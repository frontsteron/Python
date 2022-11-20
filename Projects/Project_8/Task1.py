# В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
# заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
# наилучшим средним баллом.

import random

numOfGroups = 5 # кол-во групп
columns = random.randint(20, 30) # кол-во учеников
students = [0] * numOfGroups
count = 0
scores = 0 # рейтиенг
numGroups = 1
GPA = 0 # средний балл
bestGroup = 0

for i in range(len(students)):
    columns =  random.randint(20, 30)
    students[i] = list(0 for _ in range(columns))
    for j in range(columns):
        students[i][j] = random.randint(2, 5) # оценки
        count += students[i][j]
    scores = count / columns

    if GPA < scores:
        GPA = scores
        bestGroup = numGroups
    print (f'Средний балл группы {numGroups} - {scores}')
    count = 0
    numGroups += 1

print('\nТаблица оценок по группам:')
for row in students:
    print(row)

print(f'\nГруппа с лучшим средним балом - №{bestGroup}')