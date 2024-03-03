from Project.inputs import askforstring, askfornum, askfordate, generate_id
from Project.project_read_write import read_project

def find_project():
    startdate = askfordate("Please Enter Start Time: ")
    project = search_project(startdate)
    print(project)

def search_project(startdate):
    all_projects = read_project()
    for project in all_projects:
        if project['Start Time'] == startdate:
                return project
    else:
         print("==== not found =====")
         return False


def view_project():
    all_projects = read_project()
    for project in all_projects:
         print(project)



