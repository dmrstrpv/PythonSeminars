# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

with open('text.txt', 'w') as data:
    data.write(input("Введите текст: "))

with open('text.txt', 'r') as data:
    text_origin = data.readline()
    text_change = text_origin.split()

print()
print(text_origin)
print()

letters = "АБВ"


def delete_words(words, text):
    text_final = ' '.join(filter(lambda t: words not in t, text))
    with open('text.txt', 'w') as x:
        x.write(f'{text_final}')
    return text_final


print(delete_words(letters, text_change))