import rsa
import json
import os
import base64


def createUser():
    """
    Метод для создания нового пользователя.
    Генерирует ключи и записывает их в файл /data/user.json
    """
    (pubkey, privkey) = rsa.newkeys(512)

    pubkey_pem = pubkey.save_pkcs1().decode('utf-8')
    privkey_pem = privkey.save_pkcs1().decode('utf-8')

    address = base64.b64encode(pubkey_pem.encode('utf-8')).decode('utf-8')

    toJSON = {
        'address': address,
        'pubkey': pubkey_pem,
        'privkey': privkey_pem
    }

    with open("../data/user.json", "w") as write_file:
        json.dump(toJSON, write_file)

    return True


def readUserKeys():
    """
    Метод для выгрузки ключей пользователя с файла /data/user.json
    Возвращает id, public key и private key.
    """
    with open("../data/user.json", "r") as read_file:
        UserKeys = json.load(read_file)

    address = UserKeys.get('address')
    pubkey = UserKeys.get('pubkey')
    privkey = UserKeys.get('privkey')

    return address, pubkey, privkey


def pubKeyPEMtoPubKey(pubkeyPEM):
    """
    Метод для восстановления публичного ключа до цифр.
    Принимает публичный ключ в формате PEM и возвращает публичный ключ в формате цифр.
    """
    pubkey = rsa.PublicKey.load_pkcs1(pubkeyPEM)
    return pubkey


def logout():
    """
    Метод для выхода пользователя из системы.
    Удаляет ключи пользователя из /data/user.json
    """
    os.remove("../data/user.json")

    return True
