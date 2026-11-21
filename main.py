from storage import add_password, get_password, list_services
from generator import generate_password
from getpass import getpass
from checks import check_master_password
import os


if not os.path.exists("vault.bin"):
    print("First launch, create a master password")
    while True:
        master = input("Master password: ")
        #master = getpass("Master password: ")
        if not check_master_password(master):
            continue
        #again = getpass("Повторите: ")
        again = input("Повторите: ")
        if master == again:
            break
        print("Пароли не совпали, попробуйте ещё раз")
else:
    master = input("Master password: ") #для ide
    #master = getpass("Master password: ")
    try:
        list_services(master)
    except ValueError:
        print("Incorrect master password")
        exit()

while True:
    print(
   ' \n 1. add password \n 2. show password \n 3. services list \n 4. generate password \n 0. exit '
    )

    a = input()

    if a == '1':

        service = input('serice:')
        login = input('login:')
        choice = input('generate password? y/n ')
        if choice == 'y':
            password = generate_password()
            print('generated password:', password)
        else:
            password = input('ur password: ')


        add_password(
            service,
            login,
            password,
            master
             )


    elif a == '2':
        password = get_password(input('service: '), master)
        if password is None:
            print('There is no such service')
        else:
            print(password)


    elif a == '3':
        clist = list_services(master)
        print(clist)


    elif a == '4':
        generatedPassword = generate_password()
        print(generatedPassword,' - generated password')

    elif a == '0':
        break
    else:
        print('invalid input')