# Semantic Visual Explorer (SVE)

Chuyển đổi văn bản phẳng thành mạng lưới thực thể tương tác, được hỗ trợ bởi AI.

## Các tính năng
- **Bản đồ ngữ nghĩa**: Tự động nhóm các khái niệm liên quan bằng cách sử dụng BERT embeddings.
- **Trực quan hóa tương tác**: Phóng to, kéo thả và khám phá các liên kết trong bản đồ tri thức 2D.
- **Flashcards trực quan**: Nhấp vào các nút (node) để tạo hình ảnh bằng AI (DALL-E 3) và xem định nghĩa.
- **NER thời gian thực**: Trích xuất con người, địa điểm và các khái niệm chính từ văn bản bất kỳ.

## Cấu trúc dự án
- **/backend**: Máy chủ FastAPI xử lý NLP và AI tạo ảnh.
- **/frontend**: Ứng dụng React (Vite) cho giao diện người dùng tương tác.

## 🚀 Cách khởi chạy (Dictionary Edition)

Dự án hiện đã được chuyển đổi sang mô hình **Bản đồ Từ điển**, giúp học sinh dễ dàng khám phá các mối liên hệ giữa các từ vựng thông dụng.

### 1. Chuẩn bị Dữ liệu (Backend)
Để tạo ra các liên kết ngữ nghĩa giữa 200 từ vựng mẫu, anh cần chạy script tiền xử lý:
- Truy cập thư mục: `cd backend`
- Chạy script: `python process_dictionary.py`
- *Lưu ý: Lần đầu tiên chạy sẽ mất khoảng 2-5 phút để hệ thống tải mô hình BERT (~400MB) về máy.*

### 2. Chạy ứng dụng thông thường
- **Backend**: `python main.py` (Cổng 8000)
- **Frontend**: `npm run dev` (Cổng 5173)

### 3. Cách sử dụng
- Khi trang web tải xong, anh sẽ thấy một mạng lưới các từ vựng lơ lửng.
- Dùng **Thanh Tìm Kiếm** bên dưới để gõ một từ bất kỳ (VD: "Sun", "Apple").
- Nhấn vào từ đó để xem định nghĩa và hình ảnh minh họa do AI vẽ.

---

## 📦 Triển khai với Docker & AWS
Dự án đã hỗ trợ sẵn Docker Compose cho việc triển khai nhanh chóng:
- Chạy: `docker-compose up --build`
- Tham khảo [AWS Guide](file:///C:/Users/My%20Computer/.gemini/antigravity/brain/fad76f5d-e423-49ad-ba4f-99f6fdcec198/aws_deployment_guide.md) để đưa sản phẩm lên mây.
"# MindMapify" 
