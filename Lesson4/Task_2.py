# Задача 2. В первом списке находится информация об
# ассортименте мороженного, во втором списке - информация
# о том, какое мороженное есть на складе. Выведите названия
# того товара, который закончился.

General_list = {"Сливочное", "Бурёнка", "Вафелька", "Сладкоежка", "Лакомка", "Эскимо"}
Storage_list = {"Сливочное", "Вафелька", "Сладкоежка"}

print(f"Закончилось: {', '.join(General_list.difference(Storage_list))}")