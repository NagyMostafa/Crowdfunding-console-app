import json

def read_project():
    try:
        filobject = open("projects.json", "r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read()
        filobject.close()
        data= data.strip('\n')
        if data:
            file_data = json.loads(data)
            return file_data
        else:
            return []

def write_project(projectdata: dict):
    data = read_project()
    data.append(projectdata)
    valid_data = json.dumps(data, indent=2)
    try:
        fileobj = open("projects.json", "w")
    except Exception as e:
        return False
    else:
        fileobj.write(valid_data)
        fileobj.close()
        return True