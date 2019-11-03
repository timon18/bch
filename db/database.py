import os
import json


def add_block(id, hash, time, nonce, proof, transactions):
    """
    Функция которая добавляет новй файл с блоком
    :param id:
    :param hash:
    :param time:
    :param nonce:
    :param proof:
    :param transaction: Массив словарей
    :return:
    """
    file_name = 'blocks//' + id + "block.json"
    block = {
        'hash'  : hash,
        'time'  : time,
        'nonce' : nonce,
        'proof' : proof,
        'transactions': transactions
    }
    with open(file_name, 'w') as file:
        json.dump(block, file, indent=2)


def write_json(data, file_name):
    """
    Функция для добавления данных в массив в JSON файл
    :param data_dict: словарь
    :param file_name: путь к файлу
    """
    try:
        file_data = json.load(open(file_name, 'r'))
    except:
        file_data = []

    file_data.append(data)

    with open(file_name, 'w') as file:
        json.dump(file_data, file, indent=2)


def add_raw_transaction(transaction):
    """
    Добавление новой транзакции в мемпул
    :param transaction: словарь
    """
    file_name = "transactions.json"
    write_json(transaction, file_name)


def get_raw_transactions(number_of_transactions):
    """
    Функция которая возврашает массив словарей транзакций
    :param number_of_transactions: количество транзакций
    :return: массив словарей
    """
    file_name = 'transactions.json'
    file_data = json.load(open(file_name, 'r'))

    if (len(file_data)<= number_of_transactions):
        return file_data
    else:
        array_trans = []
        for i in range(number_of_transactions):
            array_trans.append(file_data[i])
        return array_trans


def delete_raw_transaction(hash):
    """
    Функция для удаления транзакции из мемпула
    :param hash: хеш транзакции
    """
    file_name = 'transactions.json'
    file_data = json.load(open(file_name, 'r'))
    new_data = []
    for i in range(len(file_data)):
        trans = file_data[i]
        if (trans["hash"] != hash):
            new_data.append(trans)

    with open(file_name, 'w') as file:
        json.dump(new_data, file, indent=2)


def add_ip_address(addr):
    """
    Добавление ip адресов
    :param addr: ip-шник
    :return:
    """
    file_name = "ip.json"
    write_json(addr, file_name)


def get_ip_address():
    """
    Функция которая возваршает массив ip адресов
    :return: массив ip-шников
    """
    file_name = "ip.json"
    file_data = json.load(open(file_name, 'r'))
    return file_data


def get_balance(account):
    """
    Возвращает баланс пользователя
    :param account: адрес
    :return:
    """
    ballance = 0
    number_of_block = (len(os.listdir('blocks/'))-1) + 1
    for id in range(number_of_block):
        file_name = 'blocks/' + str(id) + 'block.json'
        file_data = json.load(open(file_name, 'r'))
        transactions = file_data['transactions']
        for i in range(len(transactions)):
            if ((transactions[i]['sender']) == account):
                ballance -= transactions[i]['amount']
            elif ((transactions[i]['recipient']) == account):
                ballance += transactions[i]['amount']

    return(ballance)


def get_prev_id_block():
    """
    Функция которая возвращает id последнего блока
    :return: id
    """
    return len(os.listdir('blocks/'))-1


def get_prev_hash():
    """
    Функция которая возвращает хеш последнего блока
    :return: хеш
    """
    id = str(len(os.listdir('blocks/'))-1)
    file_name = 'blocks/' + id + 'block.json'
    file_data = json.load(open(file_name, 'r'))
    return file_data['hash']


