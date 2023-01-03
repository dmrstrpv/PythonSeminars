
def greeting():
    print('Hello!')
    print('Выберите 1 - калькулятор, 2 - конвертер')
    select = int(input())
    return select


def get_math_example():
    example = input("Введите выражение ")
    return example


def view_result(result):
    return print(f"Результат = {result}")


def get_mass():
    mass = input("Введите массу в кг: ")
    return mass
