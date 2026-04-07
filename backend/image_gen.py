import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class ImageGenerator:
    def __init__(self):
        self.api_key = os.getenv("PIXABAY_API_KEY")
        self.base_url = "https://pixabay.com/api/"

    async def generate_image(self, prompt: str) -> str:
        """Lấy hình ảnh minh họa miễn phí từ Pixabay."""
        if not self.api_key:
            return f"https://placehold.co/600x400/0a0a0c/ffffff?text={prompt}"
        
        try:
            async with httpx.AsyncClient() as client:
                params = {
                    "key": self.api_key,
                    "q": prompt,
                    "image_type": "illustration",
                    "orientation": "horizontal",
                    "per_page": 3,
                    "safesearch": "true"
                }
                response = await client.get(self.base_url, params=params)
                data = response.json()
                
                if data["hits"] and len(data["hits"]) > 0:
                    # Lấy hình ảnh đầu tiên
                    return data["hits"][0]["webformatURL"]
                
                # Nếu không có minh họa, thử bỏ lọc image_type=illustration
                params["image_type"] = "photo"
                response = await client.get(self.base_url, params=params)
                data = response.json()
                if data["hits"] and len(data["hits"]) > 0:
                    return data["hits"][0]["webformatURL"]

                return f"https://placehold.co/600x400/0a0a0c/ffffff?text={prompt}"
        except Exception as e:
            print(f"Lỗi khi lấy ảnh từ Pixabay: {e}")
            return f"https://placehold.co/600x400/0a0a0c/ffffff?text={prompt}"
