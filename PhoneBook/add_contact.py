
# Запись конакта в телефонную книгу

def add_contact():
    contact = []
    name = input('Введите имя: ')
    contact.append(name.title())
    sirname = input('Введите фамилию: ')
    contact.append(sirname.title())
    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)
    any_info = input('Чей оператор: ')
    contact.append(any_info.title())
    print('Абонент записан: ', contact)
    return contact