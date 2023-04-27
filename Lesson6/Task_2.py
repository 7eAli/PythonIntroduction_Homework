# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите
# программу, которая определяет, есть в массиве
# последовательность из трёх элементов, совпадающая с
# введённым числом.

import random

numbers = [random.randint(0, 9) for i in range(15)]
print(numbers)
number = int(input("Введите трехзначное число: "))
check = 0
count = 0
if number > 99 and number < 1000:
    for i in range(2, len(numbers)):
        check = numbers[i - 2] * 100 + numbers[i - 1] * 10 + numbers[i]
        if check == number:
            count += 1
        check = 0
else:
    print("Вы ввели не трехзначное число")


if count > 0:
    print(f"В массиве есть последовательность элементов, совпадающая с введенным числом, и она встречается {count} раз")
