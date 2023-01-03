# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.


# list_num = [i for i in range(10, 100)]
# result = sum(map(lambda x: x**2, (filter(lambda x: x%9 == 0, list_num))))
# print(result)

print(sum(map(lambda x: x**2, (filter(lambda x: x%9 == 0, range(10, 100))))))
