# 🚲 Dự Án: Dự Báo Nhu Cầu Thuê Xe Đạp (Seoul Bike Sharing Demand)

Bài tập lớn môn nhập môn trí tuệ nhân tạo / Khoa học dữ liệu. Đề tài ứng dụng Machine Learning để dự đoán số lượng xe đạp được thuê theo giờ dựa trên điều kiện thời tiết và thời gian.

---

## 📂 Cấu trúc thư mục dự án
```text
btaplon/
│
├── data/
│   └── SeoulBikeData.csv       # Bộ dữ liệu gốc (UCI)
│
├── models/
│   └── bike_model.pkl          # Mô hình máy học đã được huấn luyện tốt nhất
│
├── notebooks/
│   └── train_model.ipynb       # Notebook chứa mã nguồn EDA, tiền xử lý và huấn luyện mô hình
│
├── app.py                      # Ứng dụng Web giao diện tương tác (Streamlit)
└── README.md                   # Tài liệu hướng dẫn dự án
⚙️ Hướng dẫn cài đặt và chạy ứng dụng
1. Cài đặt các thư viện phụ thuộc
Mở terminal tại thư mục dự án và chạy lệnh sau để cài đặt các thư viện cần thiết:

Bash


pip install pandas numpy matplotlib scikit-learn streamlit joblib
2. Chạy ứng dụng giao diện web (Streamlit)
Khởi chạy ứng dụng dự đoán thời gian thực bằng lệnh:

Bash


python -m streamlit run app.py
Sau khi chạy, sao chép đường dẫn Local URL (ví dụ: http://localhost:8501) dán vào trình duyệt web để trải nghiệm giao diện.

📊 Phương pháp thực hiện
Tiền xử lý dữ liệu (EDA): Xử lý định dạng ngày tháng, chuyển đổi các biến phân loại (Mùa, Ngày lễ, Ngày hoạt động) sang dạng số bằng One-Hot Encoding.

Huấn luyện mô hình: Thử nghiệm mô hình Baseline (Linear Regression) và mô hình nâng cao (HistGradientBoostingRegressor).

Đánh giá: Sử dụng các độ đo MAE, RMSE và R² Score để lựa chọn mô hình tối ưu nhất rồi lưu lại dưới dạng file bike_model.pkl.

Triển khai: Xây dựng giao diện web trực quan cho phép người dùng tùy chỉnh thông số đầu vào và xem biểu đồ mô phỏng xu hướng 24 giờ.
