# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.

NumberDay_week = int(input('Введите цифру, обозначающую день недели - '))
if   NumberDay_week == 1: print("Понедельник") #если
elif NumberDay_week == 2: print("Вторник")  #а если
elif NumberDay_week == 3: print("Среда")
elif NumberDay_week == 4: print("Четверг")
elif NumberDay_week == 5: print("Пятница")
elif NumberDay_week == 6: print("Суббота")
elif NumberDay_week == 7: print("Воскресенье")
else:                     print("Нет такого дня") #иначе