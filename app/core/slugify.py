import re
import unicodedata


def slugify(text: str) -> str:
    """Простой slugify — латиница, цифры, дефисы"""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text)
    return text.strip("-").lower()
