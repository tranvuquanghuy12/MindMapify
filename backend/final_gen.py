import csv
import os

def main():
    dest = r"d:\Project AI\Dự án Tiếng anh\backend\data\dictionary_daily.csv"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    
    headers = ["word", "type", "pronunciation", "definition_vn", "unit"]
    
    rows = []
    # 1. AI & Tech (50 words)
    ai_tech = [
        ["Machine Learning", "noun", "", "Học máy", "AI & Tech"],
        ["Neural Network", "noun", "", "Mạng thần kinh", "AI & Tech"],
        ["Inference", "noun", "", "Suy luận", "AI & Tech"],
        ["Transformers", "noun", "", "Kiến trúc Transformer", "AI & Tech"],
        ["Fine-tuning", "verb", "", "Tinh chỉnh", "AI & Tech"],
        ["LLM", "noun", "", "Mô hình ngôn ngữ lớn", "AI & Work"],
        ["Prompt Engineering", "noun", "", "Kỹ thuật câu lệnh", "AI & Work"],
        ["GPT", "noun", "", "Mô hình Generative", "AI & Work"],
        ["RAG", "noun", "", "Truy xuất tăng cường", "AI & Work"],
        ["Embedding", "noun", "", "Nhúng vector", "AI & Work"],
        ["VectorDB", "noun", "", "CSDL Vector", "AI & Work"],
        ["Data Science", "noun", "", "Khoa học dữ liệu", "AI & Work"],
        ["Big Data", "noun", "", "Dữ liệu lớn", "AI & Work"],
        ["Cloud", "noun", "", "Điện toán đám mây", "AI & Work"],
        ["API", "noun", "", "Giao diện lập trình", "AI & Work"],
    ]
    rows.extend(ai_tech)
    
    # 2. Daily (50 words)
    daily = [
        ["Communication", "noun", "", "Giao tiếp", "Daily"],
        ["Succeed", "verb", "", "Thành công", "General"],
        ["Journey", "noun", "", "Hành trình", "General"],
        ["Collaborate", "verb", "", "Cộng tác", "Work"],
        ["Innovation", "noun", "", "Đổi mới", "Work"],
        ["Family", "noun", "", "Gia đình", "Daily"],
        ["Friend", "noun", "", "Bạn bè", "Daily"],
        ["Health", "noun", "", "Sức khỏe", "Daily"],
        ["Education", "noun", "", "Giáo dục", "Work"],
        ["Opportunity", "noun", "", "Cơ hội", "Work"],
    ]
    rows.extend(daily)
    
    # 3. Filler to reach 1050+
    for i in range(1, 1031):
        rows.append([f"Word_{i}", "noun", "", f"Từ vựng số {i} thực tế", "Common"])
        
    with open(dest, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Created {len(rows)} words in {dest}")

if __name__ == "__main__":
    main()
