# Задача 1. Создайте список. Запишите в него N первых
# элементов последовательности Фибоначчи.

length = int(input("Введите длину последовательности Фибоначчи: "))

sequence = [''] * length
sequence[0] = sequence[1] = 1

for i in range(2, length):
    sequence[i] = sequence[i - 1] + sequence[i - 2]

print(sequence)