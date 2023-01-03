# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Var1
numbers = [2, 3, 5, 9, 3]


def odd_sum(num):
    sum_num = 0
    for i in range(len(num)):
        if i % 2 != 0:
            sum_num += num[i]
    return sum_num


print(numbers)
print(f"Сумма элементов списка, стоящих на нечётной позиции: {odd_sum(numbers)}")

# Var2
print(f'Сумма чисел, на нечётных позициях: {sum(numbers[index] for index in range(1, len(numbers), 2))}.')
