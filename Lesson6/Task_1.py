# Задача 1. Дано натуральное число N. Найдите значение
# выражения:
# N + NN + NNN
# N может быть любой длины.

number = input("Введите число: ")
number = int(number) + int(number + number) + int(number + number + number)
print(number)