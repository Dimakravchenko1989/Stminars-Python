# Задача 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный. 



    # *Пример:* 
    
    # 2+2 => 4; 
    
    # 1+2*3 => 7; 
    
    # 1-2*3 => -5;

text = input('Введите выражение с пробелом: ')
text = text.split()

for i in range(len(text)):
    if text[i] != '+' and text[i] != '-' and text[i] != '/' and text[i] != '*':
        text[i] = int(text[i])

print(text)
new_text =[]

for i in range(len(text)):
    if text [i] == '+' or text[i] == '-':
        new_text.append(text[i-1])
        new_text.append(text[i])
    elif text[i]== '*':
        new_text.append(text[i-1] * text[i+1])
    elif text[i] =='/':
        new_text.append(text[i-1] / text[i+1])
print(new_text)

result = new_text[0]

for i in range(len(new_text)):
    if new_text[i] =='+':
        result += new_text[i+1]
    elif new_text[i] == '-':
        result -= new_text[i+1]
print(result)



