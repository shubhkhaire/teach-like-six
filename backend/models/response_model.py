from pydantic import BaseModel
from typing import Optional

class ExplainerResponse(BaseModel):
    topic: str
    text: str
    image_url: Optional[str] = None
    voice_url: Optional[str] = None
