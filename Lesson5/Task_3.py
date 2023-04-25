# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в
# списке. Удалите все повторяющиеся элементы.

import random

def Find_same(list_of_numbers):
    elements = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,}
    result = 0
    for el in list_of_numbers:
        elements[el] += 1
    for i in range(1, 11):
        if elements[i] > 1:
            result += elements[i]    
    return result


size = int(
            input("Введите размер списка: "))
numbers = [random.randint(1, 10) for i in range(size)]
print(numbers)
print(f"Совпадающих элементов: {Find_same(numbers)}")
unique_elements = set(numbers)
print(unique_elements)

