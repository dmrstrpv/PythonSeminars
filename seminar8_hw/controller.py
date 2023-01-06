import view
import model
import logging


logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main():
    select = view.menu()
    if select == 1:
        logging.info("Данные от пользователя получены")
        emp = model.get_lists()
        view.employees(emp)
        logging.info("OK")
    elif select == 2:
        logging.info("Данные от пользователя получены")
        data = view.add_employees()
        model.add_employee_to_list(data)
        logging.info("OK")
    elif select == 3:
        logging.info("Данные от пользователя получены")
        change, string = view.update_employee()
        model.update_employee(change, string)
        logging.info("OK")
    elif select == 4:
        logging.info("Данные от пользователя получены")
        number = view.delete()
        model.delete(number)
        logging.info("OK")
    elif select == 5:
        logging.info("Данные от пользователя получены")
        emp = model.data_export()
        view.employees(emp)
        logging.info("OK")
    elif select == 6:
        logging.info("Данные от пользователя получены")
        data = view.data_input()
        model.data_import(data)
        logging.info("OK")



