# 📧 Gmail Spam Classifier

## 📌 Giới thiệu

**Gmail Spam Classifier** là dự án Machine Learning dùng để phân loại nội dung email thành hai nhóm:

- **🚫 Spam**: thư rác, quảng cáo, nội dung không mong muốn
- **✅ Ham**: thư hợp lệ, thư bình thường

Mục tiêu của dự án là xây dựng một hệ thống phân loại văn bản đơn giản nhưng hiệu quả, áp dụng các kỹ thuật xử lý ngôn ngữ tự nhiên cơ bản và các mô hình học máy phổ biến để hỗ trợ nhận diện thư rác tự động.

Dự án phù hợp cho các mục đích:

- 🎓 Học tập môn **Học máy**
- 🧠 Thực hành bài toán **Text Classification**
- 💻 Làm bài tập lớn hoặc demo ứng dụng phân loại email bằng Python

---

## 🎯 Mục tiêu của dự án

Dự án được xây dựng nhằm:

- 🧹 Tiền xử lý dữ liệu email trước khi huấn luyện
- 🔤 Biểu diễn văn bản bằng phương pháp **TF-IDF**
- 🤖 Huấn luyện và so sánh nhiều mô hình phân loại
- 📊 Đánh giá hiệu quả mô hình trên tập dữ liệu kiểm thử
- 🌐 Triển khai giao diện web đơn giản bằng **Streamlit** để nhập nội dung email và dự đoán kết quả

---

## ⚙️ Công nghệ sử dụng

Dự án sử dụng các công nghệ và thư viện chính sau:

- **🐍 Python**: ngôn ngữ lập trình chính
- **📚 Scikit-learn**: xây dựng và huấn luyện mô hình Machine Learning
- **📝 TF-IDF**: chuyển đổi văn bản thành vector đặc trưng
- **🎨 Streamlit**: xây dựng giao diện web đơn giản để demo mô hình

---

## 🤖 Các mô hình được sử dụng

Trong dự án, các mô hình phân loại được thử nghiệm bao gồm:

- **Naive Bayes**
- **SVM (Support Vector Machine)**
- **Random Forest**

Các mô hình này được huấn luyện trên dữ liệu email đã qua tiền xử lý và vector hóa bằng TF-IDF, sau đó so sánh hiệu năng để lựa chọn mô hình phù hợp nhất.

---

## 🔄 Quy trình xử lý của hệ thống

Hệ thống hoạt động theo quy trình sau:

1. 📥 Đọc dữ liệu email từ file dữ liệu
2. 🧹 Làm sạch nội dung văn bản
3. 🔡 Chuyển đổi văn bản thành vector bằng **TF-IDF**
4. ✂️ Chia dữ liệu thành tập huấn luyện và tập kiểm thử
5. 🏋️ Huấn luyện các mô hình Machine Learning
6. 📈 Đánh giá kết quả dự đoán
7. 💾 Lưu mô hình tốt nhất để sử dụng cho ứng dụng web
8. 🌍 Triển khai giao diện dự đoán bằng Streamlit

---

## 📁 Cấu trúc thư mục dự án

Ví dụ cấu trúc thư mục:

```bash
gmail-spam-classifier/
│
├── data/
│   └── emails.csv
│
├── models/
│   └── trained_model.pkl
│
├── notebooks/
│   └── exploration.ipynb
│
├── run.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── utils.py
```

### 🧾 Ý nghĩa các file chính

- `run.py`: file dùng để huấn luyện mô hình
- `streamlit_app.py`: file chạy giao diện web bằng Streamlit
- `requirements.txt`: danh sách thư viện cần cài đặt
- `data/emails.csv`: tập dữ liệu email
- `models/trained_model.pkl`: file mô hình đã huấn luyện
- `README.md`: tài liệu hướng dẫn sử dụng dự án

---

## 🖥️ Yêu cầu môi trường

Trước khi chạy dự án, cần cài đặt:

- **Python 3.9+** hoặc mới hơn
- `pip` để quản lý thư viện

Khuyến nghị tạo môi trường ảo để tránh xung đột thư viện.

---

## 🚀 Hướng dẫn cài đặt

### 1️⃣ Bước 1: Clone hoặc tải source code

```bash
git clone <repo-url>
cd gmail-spam-classifier
```

Hoặc tải project về máy và mở thư mục dự án bằng VS Code / Terminal.

### 2️⃣ Bước 2: Tạo môi trường ảo

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Bước 3: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## 🗂️ Định dạng dữ liệu đầu vào

Tập dữ liệu nên được lưu dưới dạng file `.csv`, ví dụ:

```csv
text,label
"Congratulations! You have won a free iPhone","spam"
"Meeting starts at 9 AM tomorrow","ham"
"Claim your reward now by clicking this link","spam"
"Please send me the report before Friday","ham"
```

### 📌 Ý nghĩa các cột

- `text`: nội dung email
- `label`: nhãn phân loại
  - `spam`
  - `ham`

Lưu ý:
- Dữ liệu cần được làm sạch tương đối để tránh lỗi encoding
- Nên dùng UTF-8 khi lưu file CSV

---

## 🏋️ Cách huấn luyện mô hình

Sau khi đã cài đặt thư viện và chuẩn bị dữ liệu, chạy lệnh sau để train model:

```bash
python run.py
```

### ✅ Kết quả của bước train

Sau khi chạy xong, chương trình có thể thực hiện các tác vụ như:

- 📥 Đọc dữ liệu
- 🧹 Tiền xử lý văn bản
- 🔡 Biến đổi văn bản bằng TF-IDF
- 🤖 Huấn luyện các mô hình
- 📊 In ra độ chính xác hoặc các chỉ số đánh giá
- 💾 Lưu mô hình tốt nhất vào thư mục `models/`

---

## 🌐 Cách chạy giao diện web

Sau khi đã huấn luyện xong mô hình, chạy ứng dụng Streamlit bằng lệnh:

```bash
streamlit run streamlit_app.py
```

Sau đó mở trình duyệt tại địa chỉ mà Streamlit cung cấp, thường là:

```bash
http://localhost:8501
```

### 🧪 Chức năng của giao diện

- ⌨️ Nhập nội dung email vào ô văn bản
- 🖱️ Nhấn nút dự đoán
- 📬 Hệ thống trả về kết quả:
  - **Spam**
  - **Ham**

---

## ✨ Ví dụ sử dụng

### Ví dụ 1

**Input**

```text
Congratulations! You have won a free voucher. Click here now!
```

**Output**

```text
Spam
```

### Ví dụ 2

**Input**

```text
Hi team, please join the meeting at 2 PM this afternoon.
```

**Output**

```text
Ham
```

---

## 📊 Đánh giá mô hình

Các chỉ số thường được sử dụng để đánh giá mô hình gồm:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

Việc đánh giá giúp xác định mô hình nào hoạt động tốt hơn trên dữ liệu kiểm thử. Trong bài toán phân loại spam, ngoài Accuracy, nên quan tâm thêm đến **Precision** và **Recall** vì dự đoán sai có thể ảnh hưởng trực tiếp đến chất lượng lọc email.

---

## ✅ Ưu điểm của dự án

- Dễ cài đặt và dễ chạy
- Sử dụng các thuật toán phổ biến, phù hợp cho sinh viên
- Có giao diện web đơn giản để demo
- Có thể mở rộng sang các bài toán phân loại văn bản khác

---

## ⚠️ Hạn chế

- Mới phân loại ở mức **Spam / Ham**
- Hiệu quả phụ thuộc nhiều vào chất lượng dữ liệu huấn luyện
- Chưa xử lý sâu các trường hợp email phức tạp như:
  - phishing tinh vi
  - email đa ngôn ngữ
  - email có nhiều HTML hoặc ký tự đặc biệt

---

## 🔮 Hướng phát triển

Trong tương lai, dự án có thể mở rộng theo các hướng sau:

- Bổ sung tập dữ liệu lớn hơn và đa dạng hơn
- Tối ưu tiền xử lý văn bản
- So sánh thêm các mô hình nâng cao
- Triển khai lưu mô hình tự động
- Phân loại nhiều nhãn hơn như:
  - Spam
  - Ham
  - Phishing
- Kết nối với API hoặc hệ thống email thực tế

---

## 🛠️ Một số lỗi thường gặp

### 1. Không cài được thư viện

Kiểm tra lại phiên bản Python:

```bash
python --version
```

Sau đó nâng cấp pip:

```bash
python -m pip install --upgrade pip
```

### 2. Lỗi không tìm thấy file dữ liệu

Kiểm tra:
- đường dẫn file CSV
- tên file dữ liệu
- vị trí đặt file có đúng với code hay không

### 3. Streamlit không chạy

Thử cài lại:

```bash
pip install streamlit
```

Rồi chạy lại:

```bash
streamlit run streamlit_app.py
```

---

## 📝 Kết luận

**Gmail Spam Classifier** là một dự án Machine Learning cơ bản nhưng có tính thực tiễn cao, giúp minh họa đầy đủ quy trình xử lý một bài toán phân loại văn bản từ dữ liệu đầu vào đến triển khai giao diện dự đoán. Dự án phù hợp để học tập, nghiên cứu và làm nền tảng cho các hệ thống lọc email thông minh trong tương lai.
