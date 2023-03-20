"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    if score < 0:
        status = "Invalid Score"
    elif score < 50:
        status = "Bad"
    elif score < 90:
        status = "Passable"
    elif score < 100:
        status = "Excellent"
    else:
        status = "Invalid Score"
    print(status)

    import random
    random_score = random.randint(1, 101)
    print(f"Random Score: {random_score}")
    random_status = get_grade(random_score)
    print(random_status)

def get_grade(score):
    if score < 0:
        status = "Invalid Score"
    elif score < 50:
        status = "Bad"
    elif score < 90:
        status = "Passable"
    elif score < 100:
        status = "Excellent"
    else:
        status = "Invalid Score"
    return status


main()
