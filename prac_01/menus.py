menu = "(H)ello\n(G)oodbye\n(Q)uit"
menu_choice_list = ["H", "G", "Q"]
name = str(input("Enter name: "))
print(menu)
menu_choice = str(input(">>> ")).title()

while menu_choice != menu_choice_list[2]:
    if menu_choice == menu_choice_list[0]:
        print(f"Hello {name}")
    elif menu_choice == menu_choice_list[1]:
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    print(menu)
    menu_choice = str(input(">>> ")).title()
print("Finished")