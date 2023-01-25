
def view():
    a = int(input('Вывод данных: \n\
        1 - по строкам\n\
        2 - по столбцам\n\
        Ваш выбор: '))
    return a



def reading_all(a):
    if a == 1:
        print('Вывод по строкам: \n')
        with open('horizontal.txt', 'r') as file:
            for line in file:
                print(line)
    if a == 2:
        print('Вывод по столбцам: \n')
        with open('vertical.txt', 'r') as file:
            for line in file:
                print(line)