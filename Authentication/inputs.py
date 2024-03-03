import re
import time
from datetime import datetime

def askforstring(message):
    while True:
        name = input(message)
        if name.isalpha():
            return name.lower()
        print("=== not vaild first name ====")

def askfornum(message):
    while True:
        try:
            num = int(input(message))
        except Exception as e:
            print("=== not vaild project total target ====")
        else:
            return num

def askforemail(message):
    while True:
        email = input(message)
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(pattern, email)):
            return email.lower()
        print("=== not vaild email ====")

def askforpassward(message):
    while True:
        passward = input(message)
        return passward.lower()
        print("=== not vaild password ====")

def askforcomfirmpassward(message, passw):
    while True:
        confirm_password = input(message)
        if confirm_password == passw:
            return True
        else:
            return False
    
def askfornumphone(message):
    while True:
        try:
            num = input(message)
            if len(num) == 11 or len(num) == 10:
                numper = int(num)
                return numper
        except Exception as e:
            print("=== please enter an numper phone: ===")


def generate_id():
    id = time.time()
    return round(id)



