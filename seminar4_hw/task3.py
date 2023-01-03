# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

list = [random.randint(0,10) for i in range(10)]
print(list)
list1 = []
[list1.append(i) for i in list if i not in list1]
print(list1)