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


def verifyTransaction(transaction):
    """
    Метод для проверки транзакции.
    Принимает транзакцию и проверяет её. Если всё ок, то возвращает True.
    """
    hash = transaction.get('hash')
    sender = transaction.get('sender')
    recipient = transaction.get('recipient')
    amount = transaction.get('amount')
    signature = transaction.get('signature')

    # TODO: Добавить проверку баланса!

    try:
        pubkey = base64.b64decode(sender).decode('utf-8')
        pubkey = rsa.PublicKey.load_pkcs1(pubkey)
    except:
        return False

    signature = base64.b64decode(signature)

    new_hash = str(sender) + str(recipient) + str(amount)
    new_hash = new_hash.encode('utf-8')
    new_hash = hashlib.md5(new_hash).hexdigest()
    if hash != new_hash:
        return False

    if rsa.verify(hash.encode('utf-8'), signature, pubkey) != 'SHA-1':
        return False

    return True