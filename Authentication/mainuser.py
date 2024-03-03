from Authentication.Registration import create_user
from Authentication.Login import login


def mainmenu():
    while True:
        print("----------------------------------")
        choice = input("""please enter
        --------------------------------
        |   r for registration         |
        --------------------------------
        |   l for login                |
        --------------------------------
        |   e for exit                 |
        --------------------------------
        ---------> """)
        
        if choice == 'r':
            create_user()
        elif choice == 'l':
            login()
        elif choice == 'e':
            exit()
        else:
            print("please enter valid choice")


if __name__ == "__main__":
    mainmenu()
