from utils.funcs import *

filename = '../data/operations.json'
def main():

    data = load_json(filename) #читает файл json
    operations = filters_operations(data) #фильтрует данные (отбирает корректные)
    sort_dict = sort_by_date(operations) # сортирует данные в обратном хронологическом порядке
    last_operation = last_five_operations(sort_dict) #отбирает последние 5 операций
    form_data = format_data(last_operation)# приводит к запрашиваемому формату

    for i in form_data:
        print(f"{i['date']} {i['description']}\n" \
             f"{i['from']} -> {i['to']}\n" \
             f"{i['amount']} {i['currency']}\n")


main()