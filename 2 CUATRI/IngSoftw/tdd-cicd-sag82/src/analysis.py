import logging
import os
import re
from .basic import count_lines, count_words, remove_punctuation


os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    filename="logs/analysis.log",
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def text_summary(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    return {
        "chars": len(text),
        "words": count_words(text),
        "lines": count_lines(text)
    }


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    text = remove_punctuation(text)
    text = text.lower()
    text = ' '.join(text.split())
    return text


def extract_emails(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    pattern = r'\b[\w\.-]+@[\w\.-]+\.\w{2,}\b'
    emails = re.findall(pattern, text)
    if emails:
        logger.info(f"Se han encontrado {len(emails)} correos electrónicos")
    else:
        logger.warning("No se encontraron correos electrónicos")
    return emails


def safe_find(text: str, word: str, fallback: str = None) -> int | str:
    if not isinstance(text, str) or not isinstance(word, str):
        raise TypeError("Los parámetros 'text' y 'word' deben ser cadenas de texto")
    index = text.find(word)
    if index != -1:
        return index
    if fallback is not None:
        return fallback
    raise ValueError(f"La palabra '{word}' no se encontró en el texto y no se proporcionó fallback")


def classify_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    text = text.strip()
    if not text:
        return "empty"
    emails = extract_emails(text)
    words = count_words(text)
    if len(emails) == 1 and text == emails[0]:
        return "email_only"
    elif words < 10:
        return "short"
    elif words >= 50:
        return "long"
    else:
        return "normal"
