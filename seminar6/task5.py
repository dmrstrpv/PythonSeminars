# Обработка текста
# Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст,
# причём число строк заранее неизвестно.
# Ваша задача – пронумеровать слова в нём, начиная с нуля,
# а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке. (В решении задачи поможет функция enumerate())

# Ехал грека через реку,
# видит грека — в реке рак.
# Сунул грека руку в реку,
# рак за руку греку — цап!

ttwister = ["Ехал Грека через реку.", "Видит Грека в реке рак.", "Сунул Грека руку в реку.", "Рак за руку Греку цап!"]

line_num = list(enumerate(ttwister))
print(line_num)
words = []

for i in ttwister:
    words.extend(i.replace('.', ' ').split())

result = list(enumerate(words))
result.sort(key=lambda x: x[1])

result = list(filter(lambda x: x[1][0].isupper(), result))

print(words)
print(result)

final_list = []
for i in result:
    if i[1] not in final_list:
        final_list.append(i[1])
        print(f"{i[0]} - {i[1]}")
