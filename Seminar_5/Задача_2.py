# Задача 2. Написать программу, которая будет удалять все слова в которых есть "абв"

# Ввод:
# привет приаб приабвет
# Вывод:
# привет приаб

list = [i for i in input('Введите строку: ').split()]
new_list = []
for i in list:
    if 'абв' not in i:
        new_list.append(i)

print(*new_list)

for i in range(len(list)):
    if 'абв' in list[i]:
        list.pop(i)
        i -= 1
print(*list)


