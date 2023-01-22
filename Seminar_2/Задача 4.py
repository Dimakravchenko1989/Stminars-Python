# Задача 4. Дан список из 5 ростов учеников, дан еще ученик, нужно сказать на какую позицию должен встать ученик. 
# Список отсортирован по уменьщению.

amount = 5
list = []

for i in range(amount):
    list.append(int(input(f'Рост {i+1}-ого ученика: ')))

height = int(input('Рост нового ученика: '))

for i in range(len(list)):
    if height > list[i]:
        print(f'Позиция ученика в шеренге: {i+1}')
        break