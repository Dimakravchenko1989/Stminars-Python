# # Задача 1.Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# user_list = ['68','scd', 'sd8ss' ]
# num = int(input('Введите число: '))
# chek = False
# for value in user_list:
#     if value.isdigit():
#         if int(value) == num:
#             print('Да')
#             chek = True
#             break
# if not chek:
#     print('Нет')
# ----------------------------------------------

# Задача 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

user_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
user_string = input('Введите строку: ')
count = 0
for i in range(len(user_list)):
    if user_list[i] == user_string:
        count += 1 
        if count == 2:
            print('Индекс элемента:')

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
stroka = input()

if list.count(stroka) < 2:
    print(-1)
else:
    ind = list.index(stroka)
    list.pop(ind)
    print(list.index(stroka)+1)

def suma(a):
    for i in range(2, a):
        if a %




N = int(input('Введите число N: '))

f = 1
for i in range(N):
    #i = i + 1
    f = i * f
    
    print(f, end=" ")