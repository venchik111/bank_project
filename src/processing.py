def filter_by_state(list_of_dicts: list[dict], filter_state: str= "EXECUTED") -> list[dict]:
    """Фильтрует лист словарей по значению ключа state"""

    filtered_dicts: list[dict] = []

    for i in list_of_dicts:
        if i["state"] == filter_state:
            filtered_dicts.append(i)

    return filtered_dicts
