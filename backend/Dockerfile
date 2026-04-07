# Sử dụng hình ảnh Python chính thức
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các công cụ cần thiết cho hệ thống
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Sao chép tệp yêu cầu và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tải mô hình SpaCy (Dòng này quan trọng khi đóng gói Docker)
RUN python -m spacy download en_core_web_sm

# Sao chép toàn bộ mã nguồn backend
COPY . .

# Mở cổng 8000
EXPOSE 8000

# Lệnh chạy ứng dụng
CMD ["python", "main.py"]
