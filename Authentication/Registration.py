from Authentication.inputs import askforstring, askforemail, askforpassward, askforcomfirmpassward, askfornumphone, generate_id
from Authentication.user_read_write import write_user


def create_user():
    First_name = askforstring("please enter your first name: ")
    Last_name = askforstring("please enter your last name: ")
    Email = askforemail("please enter your email: ")
    Password = askforpassward("please enter your password: ")
    Confirm_password = askforcomfirmpassward("please enter your confirm password: ",Password)
    Mobile_phone = askfornumphone("please enter your Egyptian Mobile phone: +20")
    user_id = generate_id()
    userdata = {"id":user_id, "First name": First_name, "Last name": Last_name, "Email": Email, "Password": Password, "Mobilephone": Mobile_phone}
    write_user(userdata)


