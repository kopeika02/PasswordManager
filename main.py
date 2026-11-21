from storage import add_password, get_password, list_services
from generator import generate_password
from getpass import getpass
from checks import check_master_password
import os


if not os.path.exists("vault.bin"):
    print("Первый запуск, придумайте мастер-пароль")
    while True:
        master = input("Мастер-пароль: ")
        #master = getpass("Мастер-пароль: ")
        if not check_master_password(master):
            continue
        #again = getpass("Повторите: ")
        again = input("Повторите: ")
        if master == again:
            break
        print("Пароли не совпали, попробуйте ещё раз")
else:
    master = input("Мастер-пароль: ") #для ide
    #master = getpass("Мастер-пароль: ")
    try:
        list_services(master)
    except ValueError:
        print("Неверный мастер-пароль")
        exit()

while True:
    print(
   ' \n 1. Добавить пароль \n 2. Показать пароль \n 3. Список сервисов \n 4. Сгенерировать пароль \n 0. Выход'
    )

    a = input()

    if a == '1':

        service = input('Cервис:')
        login = input('Логин:')
        choice = input('Сгенерировать пароль? y/n ')
        if choice == 'y':
            password = generate_password()
            print('Сгенерирован пароль:', password)
        else:
            password = input('Ваш пароль: ')


        add_password(
            service,
            login,
            password,
            master
             )


    elif a == '2':
        password = get_password(input('Сервис: '), master)
        if password is None:
            print('Такого сервиса нет')
        else:
            print(password)


    elif a == '3':
        clist = list_services(master)
        print(clist)


    elif a == '4':
        generatedPassword = generate_password()
        print(generatedPassword,' - сгенерированый пароль')

    elif a == '0':
        break
    else:
        print('Нет такого пункта')