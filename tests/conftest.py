from typing import Any

import pytest


@pytest.fixture
def operations() -> list[dict[str, str]]:
    return [
        {"state": "EXECUTED", "date": "2023-08-26T10:00:00"},
        {"state": "CANCELED", "date": "2023-07-03T10:00:00"},
        {"state": "EXECUTED", "date": "2023-09-10T10:00:00"},
    ]


@pytest.fixture
def rub_transaction() -> dict[str, Any]:
    return {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "name": "руб.",
                "code": "RUB",
            },
        }
    }


@pytest.fixture
def usd_transaction() -> dict[str, Any]:
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "USD",
                "code": "USD",
            },
        }
    }
