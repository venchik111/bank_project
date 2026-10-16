from functools import wraps


def log(filename: str | None = None):
    """Логирует выполнение функции в файл или консоль."""

    def decorator(func):
        """Принимает функцию, которую необходимо декорировать."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Выполняет функцию и записывает информацию о ее работе."""

            def write_log(message: str) -> None:
                """Записывает сообщение в файл или выводит в консоль."""
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

            write_log(f"Начало выполнения функции {func.__name__}")

            try:
                result = func(*args, **kwargs)

                write_log(
                    f"Функция {func.__name__} успешно выполнена. "
                    f"Результат: {result}"
                )

                return result

            except Exception as error:
                write_log(
                    f"Функция {func.__name__} завершилась с ошибкой "
                    f"{type(error).__name__}. "
                    f"Входные параметры: {args}, {kwargs}"
                )
                raise

            finally:
                write_log(f"Конец выполнения функции {func.__name__}")

        return wrapper

    return decorator
