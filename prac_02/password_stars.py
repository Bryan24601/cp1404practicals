def main():
    minimum_length = 8
    password = get_password(minimum_length)
    asterisk_printing(password)


def asterisk_printing(password):
    for i in password:
        print("*", end='')


def get_password(minimum_length):
    password = str(input("Password: "))
    while len(password) < minimum_length:
        print("Invalid Password Length")
        password = str(input("Password: "))
    return password


main()