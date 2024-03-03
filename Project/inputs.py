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

def askfordate(message):
    while True:
        try:
            date_str = input(message)
            date = datetime.strptime(date_str,'%Y-%m-%d')
            start = str(date)
        except Exception as e:
            print(e)
            print("=== not vaild project date ====")
        else:
            return start

def generate_id():
    id = time.time()
    return round(id)



