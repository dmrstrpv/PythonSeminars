# На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк, которые надо будет отсортировать

lines = []
numbers = int(input("Введите нстуральное число: "))
for i in range(numbers):
    line = input(f"Введите {i + 1} строку: ")
    lines.append(line)

lines.sort(key=lambda x: len(x))
print(*lines, sep='\n')