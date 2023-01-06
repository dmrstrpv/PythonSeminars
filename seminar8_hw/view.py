import csv

def menu():
    print("Вберите: \n 1 - Показать \n 2 - Добавить \n 3 - Изменить \n 4 - Удалить \n 5 - Выгрузить \n 6 - Загрузить")
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6]:
            raise ValueError
        return select
    except Exception:
        print("Упс")
        exit()


def employees(list):
    print("Список: ")
    for i, worker in enumerate(list, 0):
        if i == 0:
            print("", *worker)
        else:
            print(i, *worker)
        print(i, *worker)


def add_employees():
    print("Введите данные: ")
    data = input().split()
    return data


def update_employee():
    print("Выберите номер сотрудника: ")
    change = int(input())
    print(change)
    print("Введите строку для перезаписи")
    string = input().split()
    return change, string


def delete():
    print("Напишите номер строки")
    number = int(input())
    return number


def data_input():
    with open('file_input.csv', mode='r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        return list(reader)
