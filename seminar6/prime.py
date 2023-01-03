# Проверка числа


def prime(n):
    result = []
    d = 2
    while d <= n ** 0.5:
        if n % d == 0:
            result.append(d)
            k = n // d
            if k != d:
                result.append(k)
        d += 1
    return result # return not result


print(prime(11))