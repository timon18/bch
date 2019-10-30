import rsa
import files


def createUser():
    """
    Метод для создания нового пользователя.
    Генерирует ключи и записывает их в файл /data/user.json
    """
    (pubkey, privkey) = rsa.newkeys(512)

    pubkey_pem = pubkey.save_pkcs1().decode()
    privkey_pem = privkey.save_pkcs1().decode()

    toJSON = {
        'id': privkey.n,
        'pubkey': pubkey_pem,
        'privkey': privkey_pem
    }

    files.createUser(toJSON)

    return True


def logout():
    """
    Метод для выхода пользователя из системы.
    Удаляет ключи пользователя из /data/user.json
    """
    files.deleteUser()
