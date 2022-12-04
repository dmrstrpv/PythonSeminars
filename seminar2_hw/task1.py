# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#Var 1
# number = float(input("Введите число "))
# sum = 0
# if number > 1:
#     while number > 0:
#         digit = number % 10
#         sum += digit
#         number //= 10
# elif number < 0:
#     number = number * -1
#     while number > 0:
#         digit = number % 10
#         sum += digit
#         number //= 10
# else:
#     number = number * 1000
#     while number > 0:
#         digit = number % 10
#         sum += digit
#         number //= 10
#
# print(sum)

#Var 2

number = input("Введите число ")
sum = 0
for i in str(number):
    if i.isdigit():
        sum += int(i)

print(number, "->" , sum)