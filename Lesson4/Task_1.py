# Задача 1. Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей числа N и
# количество этих множителей.

def Check_Prime(num):
    count = 0
    divider = 1
    while divider < num:
        if num % divider == 0:
            count += 1
        divider += 1
    if count == 1: return True
    else: return False

def Get_Prime(num):
    count = 0
    test_num = 0    
    while count != num:
       test_num += 1
       if Check_Prime(test_num) == True:
           count += 1       
    return test_num

number = int(input("Введите число для разложения на простые множители: "))

prime_factors = list()
count = 1

while number != 1:
    if number % Get_Prime(count) == 0:
        number /= Get_Prime(count)
        prime_factors.append(Get_Prime(count))
    else:
        count += 1
print(prime_factors)
