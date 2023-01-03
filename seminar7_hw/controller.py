import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main_function():
    try:
        select = view.greeting()
        if select == 1:
            logging.info("Новая запись: ")
            write_file = model.input_data()
            result = model.write_data(write_file)
            view.view_result(result)
        elif select == 2:
            logging.info("Контакты")
            contacts = model.read_data()
            output = model.read_data()
            view.view_result(output)
    except Exception as error:
        logging.warning(f"Ошибка {error}")