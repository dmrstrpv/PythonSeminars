# Дан список чисел. Вывести из него только простые числа.

numbers = [15, 2, 3, 31]


def primes(n):
    count = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            count += 1
    if count > 0:
        return False
    return True


result = list(filter(primes, numbers))
print(result)