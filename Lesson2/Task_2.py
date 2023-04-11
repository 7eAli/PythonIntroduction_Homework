# Задача 2. Выведите таблицу истинности для выражения
# ¬(X ∧ Y) ∨ Z.

print("_________________")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"| {x} | {y} | {z}", end=" | ")
            if not (x and y) or z:
                print("1 |")
            else:
                print("0 |")
            print("-----------------")
