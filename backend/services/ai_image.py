import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

async def generate_image(topic: str, caption_text: str = None) -> str:
    """
    Generate a comic-style image that matches the simplified caption_text.
    Returns a URL to the created image or a placeholder fallback.
    """

    prompt = f"Create a cute, comic-style, kid-friendly single-panel illustration for the concept: {topic}. Keep it simple, bright colors, bold outlines. Include a tiny caption that shows the main analogy. Do not include copyright logos."
    if caption_text:
        prompt += f" Caption idea: {caption_text[:120]}"

    try:
        # Using OpenAI images API (DALL·E style)
        r = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        url = r["data"][0]["url"]
        return url
    except Exception as e:
        # fallback placeholder image (you can host a local placeholder)
        return "https://via.placeholder.com/800x600.png?text=Comic+Placeholder"
