mport json
from datetime import datetime

filename = 'data/operations.json'
def load_json(filename):
    '''Функция чтения файла формата json'''
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def filters_operations(data):
    '''
    Возвращает отфильтрованные операции, убирает операции без необходимых данных
    :param data: список всех операций
    :return: список отфильтрованных операций
    '''
    operations = []
    for operation in data:
        if all(key in operation and operation[key] for key in ["state", "date", "description", "from", "to", "operationAmount"]):
            if operation.get("state") == "EXECUTED":
                operations.append(operation)
    return operations

def sort_by_date(operations):
    '''
    Сортирует по дате, от большей к меньшей
    '''
    return sorted(operations, key=lambda x: x['date'], reverse=True)

def last_five_operations(data):
    '''
    Возвращает список последних операций
    :param data: список операций
    :return: спиcок последних операций
    '''
    return data[:5]

def get_format_date(operations):
    '''
    Возвращает дату в формате ДД.ММ.ГГГГ
    '''
    date_format = datetime.fromisoformat(operations["date"])
    return date_format.strftime("%d.%m.%Y")

def get_info_from(str):
    '''Возвращает данные о карте в замаскированном виде'''

    card_number = str.split()[-1]
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}{'*' * 2} **** {card_number[-4:]}"
    new_str = str.replace(card_number, masked_card_number)
    return new_str

def get_info_to(str):
    '''Возвращает данные о счете в замаскированном виде'''

    account_number = str.split()[-1]
    masked_account_number = f"**{account_number[-4:]}"
    new_str = str.replace(account_number, masked_account_number)
    return new_str

def format_data(data):
    '''Приводит данные к требуемому формату'''
    format_data_operations = []
    for operation in data:
        date = get_format_date(operation)
        from_ = get_info_from(operation['from'])
        to = get_info_to(operation['to'])

        format_data_operations.append(
            {"date": date,
            "description": operation["description"],
            "from": from_,
            "to": to,
            "amount": operation['operationAmount']['amount'],
            "currency": operation['operationAmount']['currency']['name']
             }
        )

    return format_data_operations

