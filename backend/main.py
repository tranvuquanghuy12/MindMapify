from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import json
from dotenv import load_dotenv

from nlp_engine import NLPEngine
from image_gen import ImageGenerator

load_dotenv()

app = FastAPI(title="Semantic Visual Explorer API")
# nlp_engine = NLPEngine() # Không cần dùng nlp_engine động nữa
image_gen = ImageGenerator()

# Cấu hình CORS cho phép frontend kết nối
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đường dẫn tới tệp dữ liệu đã tính toán trước
GRAPH_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "graph_data.json")

@app.get("/graph")
async def get_graph(mode: str = "grade8"):
    filename = "graph_grade8.json" if mode == "grade8" else "graph_daily.json"
    file_path = os.path.join("data", filename)
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"nodes": [], "links": []}
    except Exception as e:
        return {"nodes": [], "links": []}

@app.get("/")
async def root():
    return {"message": "SVE Dictionary API đang hoạt động"}

@app.post("/generate-image")
async def generate_image(keyword: str):
    """Tạo hình ảnh minh họa cho một từ khóa."""
    try:
        url = await image_gen.generate_image(keyword)
        return {"image_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi tạo ảnh: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
