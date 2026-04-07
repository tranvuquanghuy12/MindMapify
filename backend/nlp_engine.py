import spacy
from sentence_transformers import SentenceTransformer, util
import numpy as np
from typing import List, Dict, Any

class NLPEngine:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        # Tải SpaCy cho nhận dạng thực thể (NER)
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # Tự động tải nếu mô hình chưa có
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
            self.nlp = spacy.load("en_core_web_sm")
        
        # Tải Sentence Transformer cho vector hóa văn bản
        self.model = SentenceTransformer(model_name)

    def extract_entities(self, text: str) -> List[Dict[str, Any]]:
        """Trích xuất các thực thể từ văn bản."""
        doc = self.nlp(text)
        entities = []
        seen = set()
        
        # Trích xuất các thực thể có tên (người, địa điểm, tổ chức...)
        for ent in doc.ents:
            if ent.text.lower() not in seen:
                entities.append({
                    "id": ent.text.lower(),
                    "label": ent.text,
                    "type": ent.label_.lower()
                })
                seen.add(ent.text.lower())
        
        # Trích xuất thêm các danh từ quan trọng như các 'khái niệm'
        for token in doc:
            if token.pos_ == "NOUN" and token.text.lower() not in seen:
                entities.append({
                    "id": token.text.lower(),
                    "label": token.text,
                    "type": "concept"
                })
                seen.add(token.text.lower())
                
        return entities

    def calculate_similarity(self, entities: List[Dict[str, Any]], threshold: float = 0.45) -> List[Dict[str, Any]]:
        """Tính toán độ tương đồng ngữ nghĩa giữa các thực thể."""
        labels = [ent["label"] for ent in entities]
        if not labels:
            return []
            
        embeddings = self.model.encode(labels, convert_to_tensor=True)
        cosine_scores = util.cos_sim(embeddings, embeddings)
        
        links = []
        n = len(labels)
        for i in range(n):
            for j in range(i + 1, n):
                score = float(cosine_scores[i][j])
                if score >= threshold:
                    links.append({
                        "source": entities[i]["id"],
                        "target": entities[j]["id"],
                        "weight": round(score, 3)
                    })
        return links

    def get_graph(self, text: str) -> Dict[str, Any]:
        """Tạo dữ liệu đồ thị từ văn bản đầu vào."""
        entities = self.extract_entities(text)
        links = self.calculate_similarity(entities)
        
        return {
            "nodes": entities,
            "links": links
        }
