def read():
    name_file = open("name", "w")
    name = input("Name: ")
    name_file.write(name)
    name_file.close()

def readline():
    name_file = open("name", "r")
    for name in name_file:
        print(f"Your name is {name}")

def readlines():


read()
readline()