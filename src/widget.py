from src import masks


def mask_account_card(number: str) -> str:
    """Маскуриует счет или карту"""
    number_split: list[str] = number.split()

    if number.startswith("Счет"):
        number_split[-1] = masks.get_mask_account(number_split[-1])
    else:
        number_split[-1] = masks.get_mask_card_number(number_split[-1])

    mask_number = " ".join(number_split)

    return mask_number


def get_date(date: str) -> str:
    """принимает на вход дату в одном формате, а возвращает в другом"""
    format_date = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return format_date
