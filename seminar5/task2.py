#2.	Напишите функцию triangle(a, b, c),
# которая принимает на вход три длины отрезков
# и определяет, можно ли из этих отрезков составить треугольник.

a = 5
b = 4
c = 3


def triangle_check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


print(triangle_check(a, b, c))