import add_contact as ac
import find_contact as fc
import user_interface
import logger

def start():
    button = user_interface.choice()
    if button == 1:
        print('Вносим нового абонента')
        contact = ac.add_contact()
        logger.log_to_file(contact)
        start()
    if button == 2:
        print('\nИщем абонента\n')
        contact = fc.find()
        logger.reading_file(contact)
        start()
    if button == 3:
        print('Просмотр всего справочника')
        logger.reading_all()
        start()
    if button == 4:
        print('Работа окончена')
        exit