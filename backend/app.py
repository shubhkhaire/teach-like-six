from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from services.ai_text import simplify_text
from services.ai_image import generate_image
from services.ai_voice import text_to_speech
from models.response_model import ExplainerResponse
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Explain I'm Six API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExplainRequest(BaseModel):
    topic: str
    include_image: bool = True
    include_voice: bool = False
    tone_age: int = 6  # default "explain like I'm six"

@app.post("/explain", response_model=ExplainerResponse)
async def explain(req: ExplainRequest):
    topic = req.topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required")

    # 1) Simplify text
    simplified = await simplify_text(topic, age=req.tone_age)

    # 2) Generate image (optional)
    image_url = None
    if req.include_image:
        image_url = await generate_image(topic, simplified)

    # 3) Generate voice (optional)
    voice_url = None
    if req.include_voice:
        voice_url = await text_to_speech(simplified)

    return ExplainerResponse(
        topic=topic,
        text=simplified,
        image_url=image_url,
        voice_url=voice_url
    )

@app.get("/health")
def health():
    return {"status": "ok"}
