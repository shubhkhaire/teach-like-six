import uuid
import os

def make_filename(prefix="out", ext="mp3"):
    uid = uuid.uuid4().hex[:12]
    fn = f"{prefix}_{uid}.{ext}"
    return fn

def safe_truncate(text: str, max_len: int = 1000):
    return text if len(text) <= max_len else text[:max_len]
