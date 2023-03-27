def read():
    name_file = open("name", "w")
    name = input("Name: ")
    name_file.write(name)
    name_file.close()


def readline():
    name_file = open("name", "r")
    name = name_file.readline()
    print(f"Your name is {name}")


def readlines():
    numbers_file = open("numbers", "r")
    numbers = numbers_file.readlines()
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    total_result = first_number + second_number
    print(total_result)
    numbers_file.close()


def for_line_in_file():
    numbers_file = open("numbers", "r")
    total = 0
    for current_line in numbers_file:
        number_to_add = int(current_line)
        total += number_to_add
    print(total)
    numbers_file.close()


read()
readline()
readlines()
for_line_in_file()
