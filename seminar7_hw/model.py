import csv


def calc(expl):
    result = eval(expl)
    return result


def convert(value):
    return int(value)*1000


def input_data():
    last = input("Введите фамилию: ")
    first = input("Введите имя: ")
    phone = input("Введите номер контакта: ")
    comment = input("Введите категорию контакта: ")
    return [last, first, phone, comment]


def write_data(w_file):
    with open("phonebook.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        for row in w_file:
            file_writer.writerow(row)


def read_data():
    with open("phonebook.csv", mode="r", encoding='utf-8') as r_file:
        reader_object = csv.reader(r_file, delimiter=";", lineterminator="\r")
        for row in reader_object:
            print(row)
