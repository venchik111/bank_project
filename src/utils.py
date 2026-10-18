import json
from typing import Any


def load_transactions(file_path: str) -> list[dict[str, Any]]:
    """Принимает путь до JSON-файла и возвращает список транзакций."""
    try:
        with open(file_path, encoding="utf-8") as file:
            transactions = json.load(file)

        if isinstance(transactions, list):
            return transactions

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
