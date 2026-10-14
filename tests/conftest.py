import pytest


@pytest.fixture
def operations():
    return [
        {"state": "EXECUTED", "date": "2023-08-26T10:00:00"},
        {"state": "CANCELED", "date": "2023-07-03T10:00:00"},
        {"state": "EXECUTED", "date": "2023-09-10T10:00:00"},
    ]
