# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.

def Check_Common_Denominator(num_1, num_2):
    if num_1 > num_2:
        max = num_1
    else:
        max = num_2
    result = False
    for i in range(2, max):
        if num_1 % i == 0 and num_2 % i == 0:
            result = True
    return result

for i in range(2, 12):
    for j in range(1, i):
        if not Check_Common_Denominator(i, j):
            print(f"{j}/{i}", end="\t")
    print()