import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def get_transaction_amount(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    headers = {"apikey": API_KEY}

    params = {
        "amount": amount,
        "from": currency,
        "to": "RUB",
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params=params,
    )

    response.raise_for_status()

    result = response.json()

    return float(result["result"])
