import json
from pathlib import Path
from typing import Any

from src.utils import load_transactions


def test_load_transactions(
    tmp_path: Path,
) -> None:
    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]

    file_path = tmp_path / "operations.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(transactions, file)

    result = load_transactions(str(file_path))

    assert result == transactions


def test_load_transactions_empty_file(
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    result = load_transactions(str(file_path))

    assert result == []


def test_load_transactions_not_list(
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "operations.json"

    data: dict[str, Any] = {
        "id": 1,
        "state": "EXECUTED",
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

    result = load_transactions(str(file_path))

    assert result == []


def test_load_transactions_file_not_found() -> None:
    result = load_transactions("file_that_does_not_exist.json")

    assert result == []
