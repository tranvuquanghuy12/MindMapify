import csv
import os

def generate_big_daily_dict(output_path):
    headers = ["word", "type", "pronunciation", "definition_vn", "unit"]
    
    # 1. AI & Work (30 từ)
    ai_work = [
        ["Neural Network", "noun", "", "Mạng thần kinh nhân tạo", "AI & Work"],
        ["Deep Learning", "noun", "", "Học sâu", "AI & Work"],
        ["Machine Learning", "noun", "", "Học máy", "AI & Work"],
        ["Large Language Model", "noun", "", "Mô hình ngôn ngữ lớn", "AI & Work"],
        ["Prompt Engineering", "noun", "", "Kỹ thuật đặt câu lệnh", "AI & Work"],
        ["Inference", "noun", "/ˈɪn.fər.əns/", "Sự suy luận", "AI & Work"],
        ["Transformer", "noun", "", "Kiến trúc Transformer", "AI & Work"],
        ["Algorithm", "noun", "/ˈæl.ɡə.rɪ.ðəm/", "Thuật toán", "AI & Work"],
        ["Fine-tuning", "verb", "", "Tinh chỉnh mô hình", "AI & Work"],
        ["Hallucination", "noun", "", "Sự ảo tưởng (IA)", "AI & Work"],
        ["Tokenization", "noun", "", "Tách token", "AI & Work"],
        ["Vector Database", "noun", "", "Cơ sở dữ liệu vector", "AI & Work"],
        ["Training Data", "noun", "", "Dữ liệu huấn luyện", "AI & Work"],
        ["GPU", "noun", "", "Bộ xử lý đồ họa AI", "AI & Work"],
        # Thêm các từ AI khác...
    ]
    
    # 2. Giao tiếp hàng ngày (tăng cường)
    basics = [
        ["Hello", "exclamation", "/həˈləʊ/", "Xin chào", "Daily"],
        ["Goodbye", "exclamation", "/ˌɡʊdˈbaɪ/", "Tạm biệt", "Daily"],
        ["Thank you", "phrase", "/θæŋk juː/", "Cảm ơn bạn", "Daily"],
        ["Family", "noun", "/ˈfæməli/", "Gia đình", "Daily"],
        ["Friend", "noun", "/frend/", "Bạn bè", "Daily"],
        ["Meeting", "noun", "/ˈmiːtɪŋ/", "Cuộc họp", "Work"],
        ["Project", "noun", "/ˈprɒdʒekt/", "Dự án", "Work"],
        ["Deadline", "noun", "/ˈdedlaɪn/", "Hạn chót", "Work"],
    ]

    # 3. Tạo 1000 từ giả lập để test đồ thị
    extra = []
    for i in range(1, 1000):
        extra.append([f"CommonWord_{i}", "noun", "", f"Nghĩa từ {i}", "General"])
    
    all_rows = ai_work + basics + extra
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(all_rows)
        
    print(f"Hoàn thành! Đã tạo {len(all_rows)} từ.")

if __name__ == "__main__":
    # Dùng đường dẫn tương đối để tránh lỗi encoding trong script
    path = os.path.join("data", "dictionary_daily.csv")
    generate_big_daily_dict(path)
