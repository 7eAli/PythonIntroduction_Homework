# Задача 3. Даны две строки. Посчитайте сколько раз
# каждый символ первой строки встречается во второй

# «one» «onetwonine» - o –
# 2, n – 3, e – 3

text_1 = input("Введите основной текст: ")
text_2 = input("Введите фрагмент текста: ")
count = list()
for i in range(0, len(text_2)):
    count.append(0)
    for j in range(0, len(text_1)):
        if text_2[i] == text_1[j]:
            count[i] += 1
    print(f"{text_2[i]} - {count[i]}")
