import hashlib
import rsa
import base64
from bch.blockchain import user


def createTransaction(recipient, amount):
    """
    Метод для создания транзакций.
    Принимает адрес отправителя и сумму. Возвращает транзакцию.
    """
    sender = user.readUserKeys()[0]
    privkey = user.readUserKeys()[2]

    # TODO: Добавить проверку баланса!

    hash = str(sender) + str(recipient) + str(amount)
    hash = hash.encode('utf-8')
    hash = hashlib.md5(hash).hexdigest()

    signature = rsa.sign(hash.encode('utf-8'), rsa.PrivateKey.load_pkcs1(privkey), 'SHA-1')
    signature = base64.b64encode(signature).decode('utf-8')

    transaction = {
        'hash': hash,
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
        'signature': signature
    }

    # TODO: Дописать создание транзакции!

    return transaction
