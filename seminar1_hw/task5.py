# 5.	Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# o	A (3,6); B (2,1) -> 5,09
# o	A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input("Введите координату x точки А "))
y1 = int(input("Введите координату y точки А "))
x2 = int(input("Введите координату x точки В "))
y2 = int(input("Введите координату y точки В "))

result = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))

print("А (",x1,",",y1,");", "B (",x2,",",y2,")" "->", result)