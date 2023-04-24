from prac_06.programming_languages import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python.language_information())

language_list = [python, ruby, visual_basic]
dynamic_language_list = []
for current_language in language_list:
    if current_language.is_dynamic() == "Dynamic":
        dynamic_language_list.append(current_language.name)

print("The dynamically typed languages are:")
for current_line in dynamic_language_list:
    print(current_line)