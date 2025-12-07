import logging
import os


os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    filename="logs/basic.log",
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def count_lines(text: str) -> int:
    if not isinstance(text, str):
        logger.error(f"Texto: ({text}) -> El argumento debe ser una cadena de texto")
        raise TypeError("El argumento debe ser una cadena de texto")
    lines = len([line for line in text.split('\n') if line.strip()])
    logger.info(f"El texto tiene {lines} líneas")
    return lines


def count_words(text: str) -> int:
    if not isinstance(text, str):
        logger.error(f"Texto: ({text}) -> El argumento debe ser una cadena de texto")
        raise TypeError("El parámetro debe ser una cadena de texto.")
    words = text.split()
    logger.info(f"El texto tiene {len(words)} palabras")
    return len(words)


def count_letters(text: str) -> int:
    if not isinstance(text, str):
        logger.error(f"Texto: ({text}) -> El argumento debe ser una cadena de texto")
        raise TypeError("El parámetro debe ser una cadena de texto.")
    count = sum(1 for char in text if char.isalpha())
    logger.info(f"El texto tiene {count} letras")
    return count


def remove_punctuation(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("El parámetro debe ser una cadena de texto.")
    punctuation = r"""¡!"#$%&'()*+,-./:;<=>¿?@[\]^_`{|}~"""
    return ''.join(char for char in text if char not in punctuation)
