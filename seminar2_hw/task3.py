#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#var1

num = int(input("Введите число: "))
sum = 0

for i in range(1, num + 1):
    sum += (1 + 1/i)**i
    print(round((1 + 1/i)**i, 2), end=" ")

print(" ")
print(round(sum))

#var2

# num = int(input("Введите число: "))
#
# def numbersequence(num):
#
#     return [round((1 + 1/num)**num, 2) for num in range(1, num + 1)]
#
# print(numbersequence(num))
# print(sum(numbersequence(num)))