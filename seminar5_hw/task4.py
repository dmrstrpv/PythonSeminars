# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('text_task4.txt', 'w') as data:
    data.write(input('Введите текст для кодировки: '))

with open('text_task4.txt', 'r') as data:
    text_origin = data.readline()
    text_change = text_origin.split()

print(text_origin)


def rle_compression(text):
    letter = ''
    previous_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != previous_char:
            if previous_char:
                letter += str(count) + previous_char
            count = 1
            previous_char = char
        else:
            count += 1
    else:
        letter += str(count) + previous_char
        return letter


text_change = rle_compression(text_origin)

with open('text_task4.txt', 'w') as data:
    data.write(f'{text_change}')

print(text_change)