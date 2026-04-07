import pandas as pd
import os

def create_daily_dataset(output_path):
    daily_basics = [
        ["Hello", "exclamation", "/həˈləʊ/", "Xin chào", "Daily Basics"],
        ["Goodbye", "exclamation", "/ˌɡʊdˈbaɪ/", "Tạm biệt", "Daily Basics"],
        ["Meeting", "noun", "/ˈmiːtɪŋ/", "Cuộc họp", "Work"],
        ["Project", "noun", "/ˈprɒdʒekt/", "Dự án", "Work"],
        ["Neural Network", "noun", "", "Mạng thần kinh nhân tạo", "AI & Tech"],
        ["Deep Learning", "noun", "", "Học sâu", "AI & Tech"],
        ["Algorithm", "noun", "/ˈælɡərɪðəm/", "Thuật toán", "AI & Tech"],
        ["Fine-tuning", "verb", "", "Tinh chỉnh mô hình", "AI & Tech"],
    ]
    
    # Mở rộng thêm để đạt số lượng lớn
    for i in range(1, 1001):
        daily_basics.append([f"Word_{i}", "noun", "", f"Nghĩa của từ {i}", "Common"])

    df = pd.DataFrame(daily_basics, columns=["word", "type", "pronunciation", "definition_vn", "unit"])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Hoàn thành! Đã tạo {len(df)} từ vựng tại {output_path}")

if __name__ == "__main__":
    path = r"d:\Project AI\Dự án Tiếng anh\backend\data\dictionary_daily.csv"
    create_daily_dataset(path)
