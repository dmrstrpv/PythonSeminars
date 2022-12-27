#
#
# def function(x):
#     return x ** 2
#
#
# result = function(5)
# print(result)
#
# result = lambda x: x ** 2
# print(result(4))


# def ispositive(n):
#     return n > 0
#
#
# list_num = [1, -5, 3, -7, 8]
# result = list(filter(ispositive, list_num))
# result = list(filter(lambda i: i > 0, list_num))
# print(result)


# def sqrt(x):
#     return x ** 2
#
#
# list_num = [1, 2, 3, 4, 5]
# result = list(map(sqrt, list_num))
# print(result)


# list = ['rrr', 'z', 'tyjuuu', 'aaaaaaaaaaa']
# list.sort(key=lambda i: len(i))
# list.sort(key=lambda i: len(i), reverse=True)
# print(list)
# print()

# list_num = [['a', 123], ['b', 66], ['c', 1], ['d', 56]]
# list_num.sort(key=lambda i: (-i[1], i[0]))
# print(list_num)
# list_num.sort()
# print(list_num)
# list_num.sort(key=lambda i: i[0])
# print(list_num)
# list_num.sort(key=lambda i: i[1])
# print(list_num)

list_num = list(range(1, 100))
print(list_num)

list_num = [i for i in range (1, 100) if i % 4 == 0]
print(list_num)

list_num = [i*10 for i in range (1, 100) if i % 4 == 0]
print(list_num)

list_num = [int(i) for i in input("Введите значения A, B, C: ")]

a, b, c = [int(i) for i in input("Введите значения A,B,C: ").split()]
print(a + b + c)