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
            logging.info("Выбран калькулятор")
            example = view.get_math_example()
            logging.info(f"Введено значение: {example}")
            result = model.calc(example)
            view.view_result(result)
            logging.info(f"Результат выведен {result}")
        elif select == 2:
            logging.info("Выбран конвертер")
            mass = view.get_mass()
            logging.info(f"Введено значение: {mass}")
            value = model.convert(mass)
            view.view_result(value)
            logging.info(f"Результат выведен {value}")
    except Exception as error:
        logging.warning(f"Ошибка {error}")
