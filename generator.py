import string
import secrets

def generate_password(length=16, use_digits=True, use_symbols=True):
    if length < 8 or length > 32:
        raise ValueError("Длина пароля должна быть не меньше 8 и не больше 32")
    else:
        alphabet = "" + string.ascii_letters
        if use_symbols:
            alphabet += string.punctuation
        if use_digits:
            alphabet += string.digits
        password = ""
        while len(password) != length:
            password += secrets.choice(alphabet)
        return password

if __name__ == "__main__":
    print(generate_password())