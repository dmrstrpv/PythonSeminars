# 3.	Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# o	x=34; y=-30 -> 4
# o	x=2; y=4-> 1
# o	x=-34; y=-30 -> 3

x = int(input("Введите координату x "))
y = int(input("Введите координату y "))

if x > 0 and y > 0:
    print("x =", x,";", "y =", y,";", " -> ", 1)
elif x < 0 and y > 0:
    print("x =", x,";", "y =", y,";", " -> ", 2)
elif x < 0 and y < 0:
    print("x =", x,";", "y =", y,";", " -> ", 3)
elif x > 0 and y < 0:
    print("x =", x,";", "y =", y,";", " -> ", 4)