# Задача 2. Дан список случайных чисел. Создайте список, в
# который попадают числа, описывающие возрастающую
# последовательность. Порядок элементов менять нельзя.

import random

def Show_Rising_Sequence(list_of_numbers, start_pos):
    result = [list_of_numbers[start_pos]]
    count = 0    
    for i in range(start_pos + 1, len(list_of_numbers) - 1):
        if list_of_numbers[i] > result[count]:
            result.append(list_of_numbers[i])
            count += 1
    return result


size = int(
            input("Введите размер списка: "))
numbers = [random.randint(1, 10) for i in range(size + 1)]
print(numbers)

sequences = []
for i in range(0, len(numbers) - 1):
    sequences.append(Show_Rising_Sequence(numbers, i))
    print(sequences[i])
