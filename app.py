import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Tải mô hình đã được lưu từ bước trước
model = joblib.load('models/bike_model.pkl')

st.title('🚲 Dự Báo Nhu Cầu Thuê Xe Đạp Theo Giờ (Seoul)')
st.write(
    'Nhập các thông số thời gian và thời tiết để dự đoán số lượng xe cần chuẩn'
    ' bị:'
)

# Tạo các thanh trượt và ô nhập liệu cho người dùng
col1, col2 = st.columns(2)

with col1:
  hour = st.slider('Chọn giờ trong ngày:', 0, 23, 12)
  temperature = st.number_input('Nhiệt độ (°C):', value=20.0)
  humidity = st.slider(' Độ ẩm (%):', 0, 100, 50)
  wind_speed = st.number_input('Tốc độ gió (m/s):', value=1.5)
  visibility = st.number_input('Tầm nhìn (10m):', value=1500.0)
  dew_point = st.number_input('Nhiệt độ điểm sương (°C):', value=10.0)

with col2:
  solar_rad = st.number_input('Bức xạ mặt trời (MJ/m2):', value=0.5)
  rainfall = st.number_input('Lượng mưa (mm):', value=0.0)
  snowfall = st.number_input('Tuyết rơi (cm):', value=0.0)
  day_of_week = st.selectbox(
      'Thứ trong tuần (0: Thứ Hai, ..., 6: Chủ Nhật):', range(7)
  )
  month = st.slider('Tháng trong năm:', 1, 12, 6)
  seasons = st.selectbox('Mùa:', ['Spring', 'Summer', 'Autumn', 'Winter'])
  holiday = st.selectbox('Ngày lễ:', ['No Holiday', 'Holiday'])
  func_day = st.selectbox('Ngày hoạt động (Functioning Day):', ['Yes', 'No'])

# Lấy danh sách các đặc trưng mà mô hình yêu cầu lúc train
model_features = model.feature_names_in_

# Xây dựng dictionary dữ liệu đầu vào cơ bản
base_input = {
    'Hour': hour,
    'Temperature(°C)': temperature,
    'Humidity(%)': humidity,
    'Wind speed (m/s)': wind_speed,
    'Visibility (10m)': visibility,
    'Dew point temperature(°C)': dew_point,
    'Solar Radiation (MJ/m2)': solar_rad,
    'Rainfall(mm)': rainfall,
    'Snowfall (cm)': snowfall,
    'DayOfWeek': day_of_week,
    'Month': month,
    'Seasons_' + seasons: 1,
    'Holiday_' + holiday: 1,
    'Functioning Day_' + func_day: 1,
}

# Tạo DataFrame với đúng các cột model yêu cầu, mặc định các cột khác là 0
input_data = pd.DataFrame(columns=model_features)
row_data = {col: base_input.get(col, 0) for col in model_features}
input_data = pd.concat([input_data, pd.DataFrame([row_data])], ignore_index=True)

# --- NÚT BẤM DỰ BÁO TẠI THỜI ĐIỂM CHỌN ---
if st.button('Dự Báo Số Lượng Xe Tại Giờ Này'):
  prediction = model.predict(input_data)[0]
  prediction = max(0, int(prediction))
  st.success(
      f'🎯 Dự kiến số lượng xe đạp cần chuẩn bị lúc {hour}h là: **{prediction}'
      ' chiếc**'
  )

st.markdown('---')

# --- BIỂU ĐỒ XU HƯỚNG 24 GIỜ ---
st.subheader('📈 Biểu đồ mô phỏng nhu cầu xe trong 24 giờ')

simulated_preds = []
for h in range(24):
  temp_df = input_data.copy()
  temp_df.loc[0, 'Hour'] = h
  pred_h = max(0, int(model.predict(temp_df)[0]))
  simulated_preds.append(pred_h)

chart_df = pd.DataFrame(
    {'Giờ trong ngày': range(24), 'Số lượng xe dự kiến': simulated_preds}
)
chart_df.set_index('Giờ trong ngày', inplace=True)

st.line_chart(chart_df)