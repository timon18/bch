import os
import json


def len_blocks():
    """
    Метод для подсчёта количества блоков у пользователя.
    Возвращает в int количество блоков у пользователя.
    """
    path, dirs, files = next(os.walk("../db/blocks"))
    files_count = len(files)

    return files_count


def createUser(toJSON):
    """
    Метод для записи ключей в файл.
    Принимает данные об созданном аккаунте в формате json и записывает в файл user.json
    """
    with open("../data/user.json", "w") as write_file:
        json.dump(toJSON, write_file)

    return True


def deleteUser():
    """
    Удаляет ключи пользователя из /data/user.json
    """
    os.remove("../data/user.json")

    return True
