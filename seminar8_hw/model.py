import csv


def get_lists():
    with open('file.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        return list(reader)


def add_employee_to_list(employee):
    with open("file.csv", mode="a", encoding='utf-8') as entry:
        writer = csv.writer(entry, delimiter=";")
        writer.writerow(employee)


def update_employee(number, string):
    try:
        with open("file.csv", mode="r", encoding='utf-8') as entry:
            reader = csv.reader(entry, delimiter=";")
            data = list(reader)
            data[number] = string
        with open("file.csv", mode="w", encoding='utf-8') as entry:
            writer = csv.writer(entry, delimiter=",", lineterminator="\r")
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вышли за границы списка")
        exit()
    except Exception:
        print("Что-то не так")
        exit()


def delete(number):
    with open("file.csv", mode="r", encoding='utf-8') as entry:
        reader = csv.reader(entry, delimiter=";")
        data = list(reader)
        del data[number]
    with open("file.csv", mode="w", encoding='utf-8') as entry:
        writer = csv.writer(entry, delimiter=",", lineterminator="\r")
        for i in data:
            writer.writerow(i)


def data_import(data):
    with open("file.csv", mode="w", encoding='utf-8') as w_data:
        file_writer = csv.writer(w_data, delimiter=";", lineterminator="\r")
        file_writer.writerow(data)


def data_export():
    with open('file.csv', mode="r", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
    with open("newfile.csv", mode="w", encoding='utf-8') as new_data:
        file_writer = csv.writer(new_data, delimiter=",", lineterminator="\r")
        file_writer.writerow(data)
