
def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника") 
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def last_name():
    name = input('Введите фамилию работника: ')
    return name

def PostJob():
    job = input('Введите должность работника: ')
    return job.lower()

def zp():
    Wallet = input('Введите сумму заработной платы в т.р.: ')
    return Wallet

# Добавить
def AddPer():
    person = input('Введите данные сотрудника в формате: id, Фамилия, имя, профессия, з/п т.р.: ')
    return person

def DelPerson():
    with open('phone_data.csv', 'r', encoding='utf-8') as data:
        print(data.read())
        who = int(input('Введите номер сотрудника для удаления: '))
        return who