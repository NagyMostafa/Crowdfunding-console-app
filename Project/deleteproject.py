from Project.inputs import askfordate , generate_id, askfornum
from Project.project_read_write import read_project, write_project
import json

def delete(user_id):
    project_id = askfornum("please enter project id: ")
    del_pro = delete_project(project_id ,user_id)

def delete_project(project_id, user_id):
    all_projects = read_project()
    for project in all_projects:
        if project['User ID'] == user_id:
            if project['Project ID'] == project_id:
                all_projects.remove(project)
                valid_data = json.dumps(all_projects, indent=2)
                fileobj = open("projects.json", "w")
                fileobj.write(valid_data)
                fileobj.close()

