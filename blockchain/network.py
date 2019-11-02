import socket
import json
import consts


def send_messgae(data, type, address):
    """
    Метод который отправляет данные по IP адресу
    :param data: Данные
    :param type: Тип данных
    :param address: IP адресс
    """

    message = {
        'type': type,
        'data': data,
    }

    j_mess = json.dumps(message)
    sock = socket.socket()

    try:
        sock.connect(('192.168.1.101', 4000))
        sock.send(j_mess.encode())
    except TimeoutError:
        print('Не удалось утановить соединение с ', address)

    sock.close()

def send_messgae_all(data, type):
    """
    Метод который отправляет данные всем пользователям сети
    IP адреса которых нам известны
    :param data:
    :param type:
    :return:
    """
    #TODO: Сделать! (но для начало нужно сделать бд)

def receive_message():
    """
    Метод который в бесконечном цикле принимает все
    входящие сообщения и передаёт их методу run_query
    """
    #TODO: Сделать! (но для начала сделать run_query)

def run_query(message):
    """
    Метод который на основе данных и типа сообщения
    вызывает нужный метод
    :param message: Данные которые были в сообщении
    :return:
    """
    ip = message.get('sender')
    type = message.get('type')
    data = message.get('data')

    if (type == consts.request_type.get("transaction")):
        pass
        # Пришла транзакция

    elif (type == consts.request_type.get("block")):
        pass
        # Пришёл блок

    #TODO: Сделай запрос цепочки блоков
    #ответ на это
    #запрос на скачивание цепочки блоков
    #ответ на это

