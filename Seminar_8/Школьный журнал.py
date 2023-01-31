import os


FILE_NAME = 'text.txt'
 
while True:
    choice = input('1-Просмотреть оценки\n2-Изменить оценки\n3-Удаление оценок\n')
    # вывод
    if choice == 1:
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                journal = file.read()
                if journal:
                    journal = eval(journal)
                    for student, lessons in journal.items():
                        print(student)
                        for lesson, mark in lessons.items():
                            print(lesson, mark, sep=' - ')
                else:
                    print('Файл пустой')
        else:
            print('Файл не существует')
    # ввод
    elif choice == '2':
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                journal = file.read()
            if journal:
                journal = eval(journal)
            else:
                journal = {}
            student = input('Введите имя ученика:')
            lesson = input('Введите предмет:')
            mark = input('Введите оценку:')
            if student in journal:
                journal[student].update({lesson: mark})
            else:
                journal[student] = ({lesson: mark})
            with open(FILE_NAME, 'w') as file:
                file.write(str(journal))
        else:
            print('Файла не существует')
    # удаление
    elif choice == '3':
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                journal = file.read()
            if journal:
                journal = eval(journal)
            else:
                journal = {}
            choice2 = input('1-Удалить ученика\n2-Удалить оценку\n')
            if choice2 == '1':
                student = (input('Имя ученика\n'))
                if student in journal:
                    print('Ученик удалён')
                    del journal[student]
                elif student not in journal:
                    print('Такого ученика нет в журнале')
            elif choice2 == '2':
                student = input('Введите имя ученика у которого нужно удалить оценку:\n')
                lesson = input('Введите предмет по которому нужно удалить оценку:\n')
                if student in journal:
                    if lesson in journal[student]:
                        del journal[student][lesson]
                    elif lesson not in journal[student]:
                        print('По этому предмету у ученика нет оценок')
                if student not in journal:
                    print('В журнале нет такого ученика')
            else:
                print('Введено неправильное значение')
            with open(FILE_NAME, 'w') as file:
                file.write(str(journal))
        else:
            print('Файла не существует')
    else:
        print('Введено неправильное значение')