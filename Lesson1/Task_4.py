# Задача 4. Напишите программу, которая на вход принимает число (N), 
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

number = int(input("Введите число: "))

counter = 1
while counter != number:
    if number > 0:
        if counter % 2 == 0:
            print(f"{counter}", end=" ")
        counter += 1
    else:
        if counter % 2 == 0:
            print(f"{counter}", end=" ")
        counter -= 1