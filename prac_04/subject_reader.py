FILENAME = "subject_data.txt"

"""
def main():
    data = get_data()
    print(data)


topic_name = []
lecturer = []
number_of_students = []

def get_data():
# def get_data(topic_name, lecturer, number_of_students):
    Read data from file formatted like: subject,lecturer,number of students.
    input_file = open("D:/JCU Stuff/Programming 1/prac_04/subject_data", "r")
    data = input_file.read()
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # topic_name.append(parts[0])
        # lecturer.append(parts[1])
        # number_of_students.append(parts[2])

        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        #print(f"{topic_name + 1}, {lecturer + 1}, {number_of_students + 1}")
    input_file.close()


main()
"""

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open("D:/JCU Stuff/Programming 1/prac_04/subject_data")
    subject_split = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_split.append(parts)
        output = []
    # for line in subject_split:
        # new_part = []
        # for new_newpart in subject_split:
        #     new_part.append(new_newpart)
        #     output.append(new_part)
        # new_part = [parts[i:i+3] for i in range(0, len(parts), 3)]
        # print(parts)  # See if that worked
        # print(f"{new_part}, {new_part + 1}")
        #new_output = [output[0], output[1]]
        # print(output[0])
    for i, v in enumerate(subject_split):
        if i == 1:
            first_subject = subject_split.pop(0)
            second_subject = subject_split.pop(0)
            print(first_subject, second_subject)
            print(f"{first_subject.pop(0)} is taught by {first_subject.pop(0)} and has {first_subject.pop(0)} students")
            print(f"{second_subject.pop(0)} is taught by {second_subject.pop(0)} and has {second_subject.pop(0)} students")
            print("----------")
    input_file.close()


main()