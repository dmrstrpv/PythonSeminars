# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#var1
# num = int(input("Введит число: "))
# product = 1
# while num > 1:
#     digit = num
#     product *= digit
#     num -= 1
#
# print(product)

num = int(input("Введит число: "))

product = 1
digit = 1

for i in range(num):
    product *= digit
    print(product, end =" ")
    digit += 1
