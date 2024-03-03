from Project.inputs import askforstring, askfornum, askfordate,generate_id
from Project.project_read_write import read_project, write_project
from Project.deleteproject import delete_project

def edit(user_id):
    project_id = askfornum("please enter project id: ")
    edit_pro = edit_project(project_id, user_id)

def edit_project(project_id,user_id):
    all_projects = read_project()
    for project in all_projects:
        if project['User ID'] == user_id:
            if project['Project ID'] == project_id:
                project['Title'] = askforstring("please enter your project title: ")
                project['Details'] = askforstring("please enter your project details: ")
                project['Total Target'] = askfornum("please enter project total target: ")
                project['Start Time'] = askfordate("please enter start time of project: ")
                project['End Time'] = askfordate("please enter end time project: ")
                projectdata = {"User ID": user_id,"Project ID": project_id, "Title": project['Title'], "Details": project['Details'],
                               "Total Target": project['Total Target'] ,
                               "Start Time": project['Start Time'] , "End Time": project['End Time'] }
                delete_project(project_id , user_id)
                write_project(projectdata)




