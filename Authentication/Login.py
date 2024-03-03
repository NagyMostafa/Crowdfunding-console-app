from Authentication.inputs import askforemail, askforpassward
from Authentication.user_read_write import read_user
from Project.mainproject import  mainmenuproject


def login():
    Email = askforemail("please enter your email: ")
    Password = askforpassward("please enter your password: ")
    user = search_user(Email, Password)
    mainmenuproject(user)

def search_user(email, password):
    all_users = read_user()
    for user in all_users:
        if user['Email'] == email:
            if user['Password'] == password:
                print("==== login successful =====")
                return user['id']
    else:
        print("==== User not found =====")