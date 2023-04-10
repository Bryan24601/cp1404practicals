get_email = input("Email: ")
name_check_answers_no = ["N", "No"]
EMAIL_DICTIONARY = {}
while get_email != "":
    username = get_email.split("@")[0]
    name = " ".join(username.split(".")).title()
    name_check = input(f"Is your name {name}? (Y/n)").title()
    if name_check in name_check_answers_no:
        name = input("Name: ")
    EMAIL_DICTIONARY[name] = get_email
    get_email = input("Email: ")

for current_name in EMAIL_DICTIONARY:
    print(f"{current_name} ({EMAIL_DICTIONARY[current_name]})")
