# 5. Реализуйте алгоритм перемешивания списка(shuffle использовать нельзя,
# другие методы из библиотеки random - можно).

import random
from random import randint

n = int(input("Введите колличество элементов "))
numbers = []
for i in range(n):
    numbers.append(randint(1, 100))
print(numbers)


def shuffle_list(numbers):
    list = numbers
    for j in range(len(list)):
        random_index = random.randint(0, len(list) - 1)
        temp = list[j]
        list[j] = list[random_index]
        list[random_index] = temp

    return list


print(shuffle_list(numbers))