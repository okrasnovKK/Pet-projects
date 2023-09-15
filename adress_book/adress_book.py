import os, sys, time
os.chdir(r'D:\proga\adress_book\kontakts') #переходим в базу данных контактов
global kontakts
path='.'
kontakts = os.listdir(path) #передаём список контактов


def search_kontakt():   #поиск и работа с контактом
    name = input('\nВведите фамилию и имя контакта, \n'
                 'для возврата в предыдущее меню нажмите "0": ') #запрашиваем у пользователя необходимый контакт
    if name == '0':
        return adress_book()
    else:
        name_kontakt = (name + '.txt')
   # проводим проверку наличия контакта
        work_with_kontakt = True
        while work_with_kontakt:
            if name_kontakt in kontakts:
                choice_2 = input('\nСписок возможных запросов: \n'
                        '1 - Посмотреть контакт \n'
                        '2 - Добавить информацию в контакт \n'
                        '3 - Изменить контакт \n'
                        '4 - Удалить контакт \n'
                        '0 - Выход из программы \n'
                        'Введите номер запроса: ')
                if choice_2 == '1':             #проверка запросов пользователя
                    kontakt = open(name_kontakt)
                    print('\n'+ kontakt.read())
                    kontakt.close()
                elif choice_2 == '2':
                    add_info_kontakt(name_kontakt)
                elif choice_2 == '3':
                    change_kontakt(name_kontakt)
                elif choice_2 == '4':
                    delete_kontakt(name_kontakt)
                elif choice_2 == '0':           #выход в предыдущее меню
                    print('\n- Возвращаю в основное меню -')
                    False
                    return adress_book()
                else:
                    print('\n-- Вы ввели неправильный запрос --')
            else:               #при отстутсвии контакта возврат в основное меню
                print('\n-- Данного контакта нет --')
                work_with_kontakt = False
                search_kontakt()
        #else:
            #adress_book()



def add_info_kontakt(name, choiсe_2_2=None):    #добавление информации в контакт
    add_info = True
    while add_info:
        choice_2_2 = input('\nВведите информацию, которую нужно добавить,\n'
                          'для возврата в предыдущее меню введите "0": ')
        if choice_2_2 == '':
            print('\n-- Вы ничего не ввели --\n')
        elif choice_2_2 == '0':
            add_info = False
        else:
            kontakt = open(name, 'a')
            kontakt.write('\n' + choice_2_2)
            kontakt.close()
            print('\n- Информация успешно добавлена -\n')
    else:
        return search_kontakt()

def change_kontakt(name):       #внесение изменений в контакт
    change_info = True
    while change_info:
        old_info = input('\nВведите, что Вы хотите заменить, \n'
                         'для выхода в предыдущее меню введите "0": ')
        if old_info == '0':
            change_info = False
        elif old_info == '':
            print('\n-- Вы ничего не ввели -- \n')
        else:
            new_info = input('\nВведите новую информацию: ')
            with open(name, 'r') as k:
                old_kontakt = k.read()
            new_k = old_kontakt.replace(old_info, new_info)
            with open(name, 'w') as k:
                k.write(new_k)
            print('\n- Данные успешно изменены- \n')
    else:
       return search_kontakt()

def delete_kontakt(name):       #удаление контакта
    print('Вы уверены, что хотите удалить контакт ' + name + '?')
    choice_4 = input('\nЕсли "ДА" - нажмите 1, если "НЕТ" - нажмите любую другую клавишу.\n'
                       'Введите запрос: ')
    if choice_4 == '1':
        way = (r'D:\\proga\\adress_book\\kontakts\\') + name
        os.remove(way)
        print('Контакт удалён')
        adress_book()
    else:
        print('Отмена операции')

def create_new_kontakt():
    name = input('\n Введите имя контакта,'
                'для возврата в предыдущее меню введите "0": ')
    if name == '0':
        return adress_book()
    elif name == '':
        print('\n вы ничего не ввели.')
        return create_new_kontakt()
    else:
        new_kontakt = (name + '.txt')
        if new_kontakt in kontakts:
            print('\n Данный контакт уже создан.'
                  '\n Возвращаю в предыдущее меню.')
            return adress_book()
        else:
            #open(new_kontakt, 'w')
            add_new_info = True
            while add_new_info:
                choice_5 = input('\nВведите информацию, которую нужно добавить,\n'
                          'для возврата в предыдущее меню введите "0": ')
                if choice_5 == '':
                    print('\n-- Вы ничего не ввели --\n')
                elif choice_5 == '0':
                    add_new_info = False
                else:
                    kontakt = open(new_kontakt, 'a')
                    kontakt.write(choice_5 + '\n')
                    kontakt.close()
                    print('\n- Информация успешно добавлена -\n')
            else:
                return adress_book()


#основное меню, запрашиваем необходимую команду на выполнение от пользователя
def adress_book():
    path = '.'
    kontakts = os.listdir(path)
    start = True
    while start:
        choice_1 = input('\nСписок возможных запросов: \n'
                    '1 - Посмотреть список контактов \n'
                    '2 - Найти контакт \n'
                    '3 - Добавить новый контакт \n'     
                    '0 - Выход из программы \n'
                    'Введите номер запроса: ')

        if choice_1 == '1':
            kontakts = (''.join(kontakts))
            kontakts = kontakts.split('.txt')
            print('\n--Список контактов:\n' + '\n'.join(kontakts))
        elif choice_1 == '2':
            return search_kontakt()
        elif choice_1 == '3':
            return create_new_kontakt()
        elif choice_1 == '0':       #окончание программы
            start = False
        else:
            print('\n-- Вы ввели неправильный запрос --\n')
    else:
        print('\n - До свидания - \n')
        time.sleep(2)
        sys.exit()

adress_book()
