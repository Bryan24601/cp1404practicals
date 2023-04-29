import datetime

from prac_07.project import Project


def main():
    # Constants
    MENU = "- (L)oad Projects\n- (S)ave Projects\n- (D)isplay Projects\n- (F)ilter by Date\n- (A)dd new Project\n- (U)pdate Project\n- (Q)uit"
    # Menu
    print(MENU)
    menu_choice = input(">>> ").title()
    while menu_choice != "Q":
        if menu_choice == "L":
            projects_list = load_file()
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "S":
            save_file(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "D":
            display_projects(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "F":
            date_filter()
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "A":
            add_project()
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "U":
            update_project()
            print(MENU)
            menu_choice = input(">>> ").title()
        else:
            print("Invalid Input")
            print(MENU)
            menu_choice = input(">>> ").title()
    print("Thank you for using custom-built project management software.")


def load_file():
    projects_file = input("Project file: ")
    try:
        with open(projects_file, "r") as file:
            project_list = []
            file.readline()
            for current_line in file:
                parts = current_line.strip().split(' ')
                current_project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                project_list.append(current_project)
        return project_list
    except FileNotFoundError:
        project_list = []
        return project_list

def save_file(projects_list):
    projects_file = input("Project file: ")
    with open(projects_file, "w") as file:
        file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for current_line in projects_list:
            writing_line = " ".join(current_line)
            file.write(writing_line)
def display_projects(projects_list):
    # Sort the projects by completion status
    incomplete_projects = []
    completed_projects = []
    for project in projects_list:
        if not project.is_complete():
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)

    # Print the incomplete projects
    print("Incomplete Projects:")
    if incomplete_projects:
        for project in incomplete_projects:
            print(project)
    else:
        print("No incomplete projects.")

    # Print the completed projects
    print("\nCompleted Projects:")
    if completed_projects:
        for project in completed_projects:
            print(project)
    else:
        print("No completed projects.")


def date_filter():
    after_date_filter = input("Show projects that start after date (dd/mm/yyyy): ")
def add_project():

def update_project():


main()