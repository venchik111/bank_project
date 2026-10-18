import json
import logging
from pathlib import Path
from typing import Any


logs_dir = Path(__file__).resolve().parent.parent / "logs"
logs_dir.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    logs_dir / "utils.log",
    mode="w",
    encoding="utf-8",
)

formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list[dict[str, Any]]:
    """Принимает путь до JSON-файла и возвращает список транзакций."""
    try:
        with open(file_path, encoding="utf-8") as file:
            transactions = json.load(file)

        if isinstance(transactions, list):
            logger.info("JSON-файл успешно прочитан")
            return transactions

        logger.error("JSON-файл содержит не список")
        return []

    except FileNotFoundError:
        logger.error("JSON-файл не найден")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка чтения JSON-файла")
        return []