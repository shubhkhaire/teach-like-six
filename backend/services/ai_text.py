import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.helpers import safe_truncate

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

async def simplify_text(topic: str, age: int = 6) -> str:
    """
    Returns a simplified explanation for `topic` tuned to a ~`age` year-old,
    using Google's Gemini model.
    """
    prompt = (
        f"Explain the topic '{topic}' like I'm {age} years old. "
        f"Use simple words, a fun analogy or story, "
        f"and keep it under 140 words."
    )
    prompt = safe_truncate(prompt, 800)

    try:
        # Use the correct Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text.strip()
        else:
            return "Sorry, I couldn't generate a simple explanation right now."
    except Exception as e:
        print("Gemini error:", e)
        return f"Sorry, Gemini API failed: {e}"
