
def PersonFinder(last_name):
    with open('phone_data.csv', 'r', encoding='utf-8') as data:
        info_list = data.read().splitlines()
        for person in info_list:
            if last_name in person:
                print(person)
# опла