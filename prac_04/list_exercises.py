def main():

    numbers = []
    number_of_numbers = int(5)
    for number_of_numbers in range(1, number_of_numbers + 1):
        # numbers = []
        number_adding = float(input(f"Number: "))
        numbers.append(number_adding)

    total = sum(numbers)
    average = total/number_of_numbers
    minimum = min(numbers)
    maximum = max(numbers)

    print(numbers)
    print(f"the first number is {numbers[0]}")
    print(f"the last number is {numbers[-1]}")
    print(f"the smallest number is {minimum}")
    print(f"the largest number is {maximum}")
    print(f"the average of the numbers is {average}")

main()


def user_checking():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    userid = str(input("Your User ID is: "))
    # print(userid)
    if userid in usernames:
        print("Access granted")
    else:
        print("Access denied")


user_checking()
