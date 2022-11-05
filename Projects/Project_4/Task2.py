# Задача 2. В первой строке файла находится информация об
# ассортименте мороженного, во второй - информация о том,
# какое мороженное есть на складе. Выведите названия того
# товара, который закончился.
# 1. «Сливочное», «Бурёнка»,
# «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька»,
# «Сладкоежка»
# Закончилось: «Бурёнка»
print('')
with open('iceCream.txt', 'r', encoding='utf-8-sig') as inf:
    assortment = set(inf.readline().rstrip().split(', '))
    availability = set(inf.readline().rstrip().split(', '))
    print(assortment, '\n') 
    print(availability)
    print(f'У нас закончился -', *assortment - availability)