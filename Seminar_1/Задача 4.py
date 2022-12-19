# Задача 4. Даны два числа, проверить, что a/b без остатка.

a,b = int(input()), int(input())

if b != 0:
    if a % b ==0:
        print('Да')
    else:
        print('Нет')
else:
    print('На ноль делить нельзя')