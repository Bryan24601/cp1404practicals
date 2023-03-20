def main():
    menu = "\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    menu_choice = input(">>> ").upper()
    menu_choice_list = ["G", "P", "S", "Q"]
    while menu_choice != menu_choice_list[3]:
        if menu_choice == menu_choice_list[0]:
            score = int(input("Score: "))
            score = valid_score(score)
            print(menu)
            menu_choice = input(">>> ").upper()
        if menu_choice == menu_choice_list[1]:
            print_result(score)
            print(menu)
            menu_choice = input(">>> ").upper()
        if menu_choice == menu_choice_list[2]:
            show_stars(score)
            print(menu)
            menu_choice = input(">>> ").upper()
    print("Farewell")


def valid_score(score):
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


def print_result(score):
    if score < 50:
        status = "Bad"
    elif score < 90:
        status = "Passable"
    elif score < 100:
        status = "Excellent"
    print(status)


def show_stars(score):
    for i in range(1, score + 1):
        print("*", end='')

main()