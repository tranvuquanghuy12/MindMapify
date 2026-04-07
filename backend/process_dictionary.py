import pandas as pd
import json
import os
from sentence_transformers import SentenceTransformer, util
import torch
import numpy as np

def get_group_id(unit):
    """Phân nhóm màu sắc dựa trên Unit hoặc Category."""
    if not unit: return 1
    # Băm tên unit thành một số từ 1-10 để đổi màu node
    return (abs(hash(str(unit))) % 10) + 1

def process_dictionary(input_csv, output_json, threshold=0.5):
    print(f"Đang đọc dữ liệu từ {input_csv}...")
    try:
        df = pd.read_csv(input_csv)
    except Exception as e:
        print(f"Lỗi đọc CSV: {e}")
        return

    # Loại bỏ các dòng trống và xử lý NaN
    df = df.dropna(subset=['word'])
    df = df.fillna("") # Thay thế tất cả NaN bằng chuỗi trống để JSON hợp lệ
    
    words = df['word'].tolist()
    
    print(f"Bắt đầu xử lý {len(words)} từ...")
    
    # Tải mô hình BERT (Sử dụng cache nếu có)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Tạo embeddings
    embeddings = model.encode(words, convert_to_tensor=True)
    
    # Tính toán độ tương đồng
    cosine_scores = util.cos_sim(embeddings, embeddings)
    
    nodes = []
    for _, row in df.iterrows():
        nodes.append({
            "id": str(row['word']).lower(),
            "label": str(row['word']),
            "type": str(row['type']),
            "pronunciation": str(row.get('pronunciation', "")),
            "definition_vn": str(row['definition_vn']),
            "unit": str(row['unit']),
            "group": get_group_id(row['unit'])
        })
    
    links = []
    n = len(words)
    for i in range(n):
        # Lấy top các từ liên quan nhất
        scores = cosine_scores[i]
        k = min(5, n)
        top_k_values, top_k_indices = torch.topk(scores, k=k)
        
        for val, idx in zip(top_k_values, top_k_indices):
            idx = int(idx)
            val = float(val)
            # Không tự nối với chính mình và chỉ lấy link trên ngưỡng
            if idx > i and val >= threshold:
                links.append({
                    "source": words[i].lower(),
                    "target": words[idx].lower(),
                    "weight": round(val, 3)
                })
                
    graph_data = {
        "nodes": nodes,
        "links": links
    }

    # Đảm bảo không còn bất kỳ giá trị phi-JSON nào (NaN, Inf)
    def clean_data(obj):
        if isinstance(obj, dict):
            return {k: clean_data(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [clean_data(v) for v in obj]
        elif isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
            return ""
        return obj

    graph_data = clean_data(graph_data)
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
        
    print(f"Hoàn thành! Đã lưu {len(nodes)} nodes và {len(links)} links vào {output_json}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="dictionary_core.csv")
    parser.add_argument("--output", default="graph_data.json")
    args = parser.parse_args()

    base_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_path, "data", args.input)
    output_path = os.path.join(base_path, "data", args.output)
    
    process_dictionary(input_path, output_path)
