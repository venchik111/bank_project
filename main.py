from src.bank_operations import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions, load_transactions_csv, load_transactions_excel


def main() -> None:
    """Запускает основную логику программы."""
    print("Привет! Добро пожаловать в программу работы " "с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choice = input()

    if user_choice == "1":
        transactions = load_transactions("data/operations.json")
        print("Для обработки выбран JSON-файл.")

    elif user_choice == "2":
        transactions = load_transactions_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")

    elif user_choice == "3":
        transactions = load_transactions_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")

    else:
        print("Некорректный пункт меню.")
        return

    available_statuses = [
        "EXECUTED",
        "CANCELED",
        "PENDING",
    ]

    while True:
        print("Введите статус, по которому необходимо выполнить " "фильтрацию.")
        print("Доступные для фильтровки статусы: " "EXECUTED, CANCELED, PENDING")

        status = input().upper()

        if status in available_statuses:
            break

        print(f'Статус операции "{status}" недоступен.')

    transactions = filter_by_state(
        transactions,
        status,
    )

    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_answer = input("Отсортировать операции по дате? Да/Нет\n").lower()

    if sort_answer == "да":
        sort_type = input("Отсортировать по возрастанию " "или по убыванию?\n").lower()

        if sort_type == "по возрастанию":
            transactions = sort_by_date(
                transactions,
                reverse=False,
            )
        else:
            transactions = sort_by_date(
                transactions,
                reverse=True,
            )

    rub_answer = input("Выводить только рублевые транзакции? Да/Нет\n").lower()

    if rub_answer == "да":
        transactions = list(
            filter_by_currency(
                transactions,
                "RUB",
            )
        )

    search_answer = input(
        "Отфильтровать список транзакций " "по определенному слову в описании? Да/Нет\n"
    ).lower()

    if search_answer == "да":
        search = input("Введите слово для поиска:\n")

        transactions = process_bank_search(
            transactions,
            search,
        )

    if not transactions:
        print(
            "Не найдено ни одной транзакции, " "подходящей под ваши условия фильтрации"
        )
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: " f"{len(transactions)}")

    for operation in transactions:
        print()
        print(operation)


if __name__ == "__main__":
    main()
