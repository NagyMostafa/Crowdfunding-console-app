from Project.inputs import askforstring, askfornum, askfordate, generate_id
from Project.project_read_write import read_project, write_project


def create_project(user_id):
    UserID=user_id
    Title = askforstring("please enter your project title: ")
    Details = askforstring("please enter your project details: ")
    Totaltarget = askfornum("please enter project total target: ")
    Start_time = askfordate ("please enter start time of project: ")
    End_time = askfordate ("please enter end time project: ")
    project_id =generate_id()
    projectdata = {"User ID": UserID,"Project ID": project_id,"Title": Title, "Details": Details,
                   "Total Target": Totaltarget, "Start Time": Start_time, "End Time": End_time}
    write_project(projectdata)
