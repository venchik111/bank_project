def filter_by_currency(list_of_dict: list[dict], key):
    """Выдает операции по валюте"""
    for operation in list_of_dict:
        if operation["operationAmount"]["currency"]["code"] == key:
            yield operation


def transaction_descriptions(transaction: list[dict]):
    """Возвращает описание каждой операции по очереди"""
    for operation in transaction:
        yield operation["description"]


def card_number_generator(start: str, end: str):
    for number in range(start, end + 1):
        card_number = f"{number:016}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
