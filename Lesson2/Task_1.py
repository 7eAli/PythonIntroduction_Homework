# Задача 1. Напишите программу, которая принимает на
# вход число N и выдает список факториалов для чисел от 1
# до N.

# пусть N = 4 -> [ 1, 2, 6, 24 ]
# (1, 1*2, 1*2*3, 1*2*3*4)

number = int(
            input("Введите число: "))
product = 1
counter = 1
print("[", end='')
while counter <= number:
    product *= counter
    if counter != number:
        print(f"{product}", end="; ")
    else:
        print(f"{product}", end=" ")
    counter += 1
print("]")
