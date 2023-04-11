# Задача 4. Задайте список из N элементов, заполненных
# числами из промежутка [-N, N]. Сдвиньте все элементы
# списка на 2 позиции вправо.

# 3 -> [2, 3, -3, -2, -1, 0, 1]

number = int(
            input("Введите число: "))

numbers = list()
if number < 0:
    number = -number
count = -number

while count != number + 1:
    numbers.append(count)
    count += 1
print(numbers)

# new_numbers = list()
# for i in range(0, len(numbers)):       
#     new_numbers.append(numbers[i - 2])

# print(new_numbers) 

numbers = numbers[len(numbers) - 2: len(numbers)] + numbers[0:len(numbers) - 2] 
print(numbers)