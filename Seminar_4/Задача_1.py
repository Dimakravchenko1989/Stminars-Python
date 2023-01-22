# Задача 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя 
# используйте пробел.Без min и max

str = input('Введите строку из чисел через пробел ').split(" ")
print(str)
min = int(str[0])
max = int(str[0])
for i in str:
    if int(i) > max: max = int(i)
    if int(i) < min: min = int(i)
print(max, min)




















