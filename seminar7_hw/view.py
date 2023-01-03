import csv


def greeting():
    print('Hello!')
    print('Выберите 1 - Новая запись, 2 - Показать')
    select = int(input())
    return select


def view_result(result):
    return print(f"Результат = {result}")

