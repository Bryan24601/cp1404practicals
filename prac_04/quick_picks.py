number_of_rows = int(input(f"How many quick picks? "))
set_of_numbers = []
import random

number_of_columns = 6
# print((number_of_rows * number_of_columns))
while len(set_of_numbers) < ((number_of_rows * number_of_columns)): # while number of numbers is less than amount, generate a new number to add to the list
    new_number = random.randint(1, 45)
    counting = set_of_numbers.count(new_number)
    if counting > 0: # if number already exists in list, do not save the number
        continue
    else: # if number does not exist, add it to the list
        set_of_numbers.append(new_number)
# print(len(set_of_numbers))
# print(set_of_numbers)


# print(set_of_numbers[4])


def slicing(original, cutting): #seperate the numbers according to how many rows are needed to be generated
    return [original[i::cutting] for i in range(cutting)]


lists = (slicing(set_of_numbers, number_of_rows))
# print(lists)
# print(len(lists))
# lists_with_commas = ",".join(lists)
# print(lists_with_commas)
# lists_no_commas = lists.replace(",", " ")
for item in lists:
    # print(item)
    item.sort() # sort in ascending order
    print('{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*item)) # align everything to the right side
