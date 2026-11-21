popularPasswords = [
    "123456789012",
    "qwertyuiopas",
    "password12345",
    "admin12345678",
    "letmein123456"
]

def check_master_password(password):
    if len(password) <= 11:
        print('The password must be at least 12 characters long.')
        return False
    if password.lower() in popularPasswords:
        print('password is in popular passwords')
        return False
    #any(c.isdigit() for c in password)
    return True

