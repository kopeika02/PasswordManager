popularPasswords = [
    "123456789012",
    "qwertyuiopas",
    "password12345",
    "admin12345678",
    "letmein123456"
]

def check_master_password(password):
    if len(password) <= 11:
        print('Длина пароля должна быть не менее 12 символов')
        return False
    if password.lower() in popularPasswords:
        print('Пароль слишком простой')
        return False
    #any(c.isdigit() for c in password)
    return True

