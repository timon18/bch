import os


def len_blocks():
    """
    Метод для подсчёта количества блоков у пользователя.
    Возвращает в int количество блоков у пользователя.
    """
    path, dirs, files = next(os.walk("../db/blocks"))
    files_count = len(files)

    return files_count
