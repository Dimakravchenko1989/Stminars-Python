# Запись конакта в телефонную книгу

def save_contact():
    contact = []
    surname = input('Введите фамилию: ')
    contact.append(surname.title())

    name = input('Введите имя: ')
    contact.append(name.title())
    
    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)

    coment = input('Описание: ')
    contact.append(coment.title())

    print('Абонент записан: ', contact)
    return contact

# Запись контакта в файлы по срокам и по столбцам

def save_file(contact):

    with open('horizontal.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]};\n')

    with open('vertical.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]}\n')
