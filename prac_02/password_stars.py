minimum_length = 8
password = str(input("Password: "))
while len(password) < minimum_length:
    print("Invalid Password Length")
    password = str(input("Password: "))
for i in password:
    print("*", end='')
