# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Задайте натуральное число "))

list = []
for i in range(1,n+1):
    if(n%i==0):
        list.append(i)

print(f'Список простых множителей числа: {n} = {list}')