def impo(some_person):
    with open('phone_data.csv', 'a', encoding='utf-8') as f:
        f.write(some_person + '\n')