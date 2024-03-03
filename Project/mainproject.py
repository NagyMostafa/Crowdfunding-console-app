from Project.addproject import create_project
from Project.searchproject import find_project,view_project
from Project.editproject import edit
from Project.deleteproject import delete

def mainmenuproject(user_id):
    while True:
        print("----------------------------------")
        choice = input("""please enter
        --------------------------------
        |   p for add project          |
        --------------------------------
        |   v for view project         |
        --------------------------------
        |   s for search project       |
        --------------------------------
        |   u for update project       |
        --------------------------------
        |   d for delete project       |
        --------------------------------
        |   e for exit                 |
        --------------------------------
        ---------> """)
        if choice == 'p':
            create_project(user_id)
        elif choice == 'v':
            view_project()
        elif choice == 's':
            find_project()
        elif choice == 'u':
            edit(user_id)
        elif choice == 'd':
            delete(user_id)
        elif choice == 'e':
            exit()
        else:
            print("please enter valid choice")


if __name__ == "__main__":
    mainmenuproject()
