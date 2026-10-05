from datetime import datetime


def filter_by_state(
    list_of_dicts: list[dict], filter_state: str = "EXECUTED"
) -> list[dict]:
    """Фильтрует список словарей по значению ключа state"""

    filtered_dicts: list[dict] = []

    for item in list_of_dicts:
        if item["state"] == filter_state:
            filtered_dicts.append(item)

    return filtered_dicts


def sort_by_date(list_of_dicts: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по значению ключа date"""

    def get_date_key(item):
        date_str = item.get("date")

        if date_str:
            return datetime.fromisoformat(date_str)

        return datetime.min

    return sorted(list_of_dicts, key=get_date_key, reverse=reverse)
