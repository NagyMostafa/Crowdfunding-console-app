import  json

def read_user():
    try:
        filobject = open("users.json", "r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read()
        filobject.close()
        data= data.strip('\n')
        if data:
            file_data = json.loads(data)
            return file_data
        return []

def write_user(userdata: dict):
    old_data = read_user()
    old_data.append(userdata)
    valid_data = json.dumps(old_data, indent=2)
    try:
        fileobj = open("users.json", "w")
    except Exception as e:
        return False
    else:
        fileobj.write(valid_data)
        fileobj.close()
        return True

