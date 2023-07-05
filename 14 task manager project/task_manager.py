# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def read_user_pass_txt() -> dict:
    # Read in user_data
    with open("user.txt", 'r') as user_file:
        user_data:list[str] = user_file.read().split("\n")

    # Convert to a dictionary
    username: str
    password: str
    username_password: dict = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    return username_password

def read_user_txt() -> list[str]:
    # Read in user_data
    with open("user.txt", 'r') as user_file:
        user_data:list[str] = user_file.read().split("\n")

    # Convert to a dictionary
    username: str
    password: str
    username_list: list = []
    for user in user_data:
        username, password = user.split(';')
        username_list.append(username)

    return username_list

def read_tasks_txt() -> list[dict]:
    # Create tasks.txt if it doesn't exist
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    with open("tasks.txt", 'r') as task_file:
        task_data: list[str] = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    task_list = []
    for t_str in task_data:
        curr_t: dict = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = \
            datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = \
            datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True \
            if task_components[5] == "Yes" else False

        task_list.append(curr_t)
        
    return task_list

def write_tasks_txt(task_list) -> bool:
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
            
        task_file.write("\n".join(task_list_to_write))
    return True

def login() -> str:
    #====Login Section====
    '''
    This code reads usernames and password from the user.txt file to 
    allow a user to login.
    '''
    # If no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    username_password = read_user_pass_txt()

    logged_in = False
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
            
    return curr_user

def reg_user() -> bool:
    '''
    Function to add a new user to the user.txt file
    '''
    username_password = read_user_pass_txt()

    while True:
        # - Request input of a new username
        new_username = input("New Username: ")

        try:
            username_password[new_username]
            print("User name already exists, add a different username")
            continue    
        except:
            break
        
    while True:
        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            username_password[new_username] = new_password
    
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
            print("New user added")        
            break
        # - Otherwise you present a relevant message.
        else:
            print("Passwords do not match")
        
    return True

def add_task() -> bool:
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    
    username_list = read_user_txt()
    
    if task_username not in username_list:
        print("User does not exist. Please enter a valid username")
        return False
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. "
                  "Please use the format specified")
    
    # Then get the current date.
    curr_date: date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task: dict = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list: list[dict] = read_tasks_txt()
    
    task_list.append(new_task)

    iswrite = write_tasks_txt(task_list)
    if iswrite == True:
        print("Task successfully added.")
    
    return True

def view_all() -> bool:
    '''
    Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''
    task_list = read_tasks_txt()
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += (f"Date Assigned: \t "
            +f"{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
        disp_str += (f"Due Date: \t "
            +f"{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n")
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        
    return True
        
def view_mine(curr_user: str) -> bool:
    '''
    Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''
    task_list: list[dict] = read_tasks_txt()

    counter = 0
    
    for i,t in enumerate(task_list):
        if t['username'] == curr_user:
            disp_str = f"Task {i+1} : \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += (f"Date Assigned: \t "
                +f"{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            disp_str += (f"Due Date: \t "
                +f"{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Task Completed: {t['completed']}"
            print(disp_str)
            counter += 1
   
    if counter == 0:
        print("No tasks found. Returning to main menu.")
        return False
    
    while True:
        task_select_str = input('''
        Select a task by number or type 
        -1 to return to main menu.
        ''')
        try:
            task_index = int(task_select_str) -1
            if task_index == -2:
                print("in task index -2")
                print(task_list)
                iswrite = write_tasks_txt(task_list)
                print(f"bbbb {iswrite}")
                if iswrite: 
                    print("Task successfully updated. \n\n")
                return True
            task_list[task_index]
        except:
            print(task_select_str+" is not a valid option.")
            continue
        
        action_select = input('''
        Select an action:
        m: Mark task done/undone
        e: Edit task
        -1: Return to main menu
        ''').lower().strip()
        if action_select == 'm':      
            task_list[task_index]['completed'] = \
                not task_list[task_index]['completed'] 
        elif action_select == "e":
            if task_list[task_index]['completed']:
                print("Task is completed, cannot edit.")
                continue
            
            while True:
                new_user = input("Current user = "
                                +task_list[task_index]["username"]
                                +" : type new username or enter to "
                                "keep username the same.")
                if new_user != "":
                    username_list: list = read_user_txt()
                    if new_user not in username_list:
                        print("User does not exist. "
                              "Please enter a valid username or "
                              "enter to keep username the same.")
                        continue            
                    task_list[task_index]["username"] = new_user
                    break
                else:
                    break
                
            while True:
                due_date_str = datetime.strftime(\
                    task_list[task_index]["due_date"], 
                    DATETIME_STRING_FORMAT)
                task_due_date = input("Current task due date = "
                                +due_date_str
                                +"\n : Enter new due date (YYYY-MM-DD) "
                                "or press enter to keep due date the same.")
                if task_due_date != "":
                    new_due_date = \
                        datetime.strptime(task_due_date, 
                                          DATETIME_STRING_FORMAT)
                    task_list[task_index]["due_date"] = new_due_date
                    break
                else:
                    break
        elif action_select == '-1':
            iswrite = write_tasks_txt(task_list)
            print(f"aaaa {iswrite}")
            if iswrite: 
                print("Task(s) successfully updated. \n\n")
            return True
        else:
            print("Action not recognised. Try again.")
            

def generate_reports() -> bool:
    task_list: list[dict] = read_tasks_txt()
    curr_date: date = date.today()
        
    task_users: list[str] = [task['username'] \
        for task in task_list]
    task_overdue: list[bool] = \
        [True if (task['assigned_date'].date() < curr_date) else False \
        for task in task_list]
    task_completed: list[bool] = [task['completed'] \
        for task in task_list]
    
    total_number_of_tasks: int = len(task_users)
    task_overdue_not_complete: list[bool] = \
        [True if ((task_overdue[i] == True) \
            and (task_completed[i] == False)) else False \
            for i in range(total_number_of_tasks)]
        
    total_number_of_completed_tasks: int = task_completed.count(True)
    total_number_of_uncompleted_tasks: int = task_completed.count(False)
    total_number_of_uncompleted_tasks_overdue: int = \
        task_overdue_not_complete.count(True)
    
    percentage_tasks_incomplete: float = \
        (total_number_of_uncompleted_tasks/total_number_of_tasks)*100.
    percentage_tasks_incomplete_and_overdue: float = \
        (total_number_of_uncompleted_tasks_overdue/total_number_of_tasks)*100.
    
    linelen = 78
    hline = "="*linelen
    
    printline_tasks = (hline, 
        f"Tasks on {curr_date.strftime(DATETIME_STRING_FORMAT)}",
        hline, 
        (f"Total number of tasks: "+(" "*38)
         +f"{total_number_of_tasks}"),
        ("Total number of completed tasks: "+(" "*28)
         +f"{total_number_of_completed_tasks}"),
        ("Total number of uncompleted tasks: "+(" "*26)
         +f"{total_number_of_uncompleted_tasks}"),
        ("Total number of tasks that are uncompleted and overdue: "
        +" "*5
        +f"{total_number_of_uncompleted_tasks_overdue}"),
        (f"Percentage of tasks that are uncompleted: "+(" "*16)
         +f"{percentage_tasks_incomplete} %"),
        (f"Percentage of tasks that are uncompleted and overdue: "
        +" "*4
        +f"{percentage_tasks_incomplete_and_overdue} %"),
        hline)
    
    with open("task_overview.txt", "w") as default_file:
        for line in printline_tasks:
            default_file.write(line+"\n")


    user_list: list[str] = read_user_txt()
    
    total_number_of_users = len(user_list)
            
    printline_users = [hline, 
        "Total number of registered users: "
        f"{total_number_of_users}", 
        "Total number of tasks that have been generated and "
        f"tracked by the system: {total_number_of_tasks}",
        hline
    ]
    
    for user in user_list:
        isuser: list[int] = \
            [i for i, task_user in enumerate(task_users) \
                if task_user == user]
        
        total_number_of_tasks_assigned_to_user = len(isuser)
        percentage_of_all_tasks_assigned_to_user = \
            (total_number_of_tasks_assigned_to_user
                /total_number_of_tasks)*100.
        if total_number_of_tasks_assigned_to_user != 0:
            number_of_tasks_assigned_to_user_completed = \
                [task_completed[i] for i in isuser].count(True)
            percentage_of_tasks_assigned_to_user_completed = \
                (number_of_tasks_assigned_to_user_completed 
                /total_number_of_tasks_assigned_to_user)*100.
            number_of_tasks_assigned_to_user_uncompleted = \
                [task_completed[i] for i in isuser].count(False)
            percentage_of_tasks_assigned_to_user_uncompleted = \
                (number_of_tasks_assigned_to_user_uncompleted 
                /total_number_of_tasks_assigned_to_user)*100.   
            number_of_tasks_assigned_to_user_overdue_not_complete = \
                [task_overdue_not_complete[i] for i in isuser].count(True)
            percentage_of_tasks_assigned_to_user_overdue_not_complete = \
                (number_of_tasks_assigned_to_user_overdue_not_complete 
                /total_number_of_tasks_assigned_to_user)*100.   
        else: 
            percentage_of_tasks_assigned_to_user_completed = 0
            percentage_of_tasks_assigned_to_user_uncompleted = 0
            percentage_of_tasks_assigned_to_user_overdue_not_complete = 0
   
        printline_users.extend(
            [f"User: {user}", "",
            f"Total number of tasks assigned to {user} : "+(" "*30)
            +f"{total_number_of_tasks_assigned_to_user: 5d}",            
            f"Percentage of all tasks assigned to {user}: "+(" "*29)
            +f"{percentage_of_all_tasks_assigned_to_user:5.1f} %", 
            f"Percentage of tasks assigned to {user} "
            "that are completed: "+(" "*14)
            +f"{percentage_of_tasks_assigned_to_user_completed:5.1f} "
            "%", 
            f"Percentage of tasks assigned to {user} "
            "that are uncompleted: "+(" "*12)
            +f"{percentage_of_tasks_assigned_to_user_uncompleted:5.1f} "
            "%", 
            f"Percentage of tasks assigned to {user} "
            "that are uncompleted and overdue: "
            f"{percentage_of_tasks_assigned_to_user_overdue_not_complete:5.1f} "
            "%",
            hline]
            )

        with open("user_overview.txt", "w") as default_file:
            for line in printline_users: 
                default_file.write(line+"\n")
                
    return True

def display_statistics(curr_user) -> bool:
    '''
    If the user is an admin they can display statistics about number
    of users and tasks.
    '''
    if curr_user == "admin":
        
        # username_list = read_user_txt()
        # task_list = read_tasks_txt()
    
        # num_users = len(username_list)
        # num_tasks = len(task_list)

        # print("-----------------------------------")
        # print(f"Number of users: \t\t {num_users}")
        # print(f"Number of tasks: \t\t {num_tasks}")
        # print("-----------------------------------")    

        if not os.path.exists("task_overview.txt") \
            or not os.path.exists("user_overview.txt"):
            generate_reports()

        with open("task_overview.txt", "r") as default_file:
            for line in default_file.readlines():
                newline = line.replace("\n","")
                print(newline)
                
        print(" ")
        with open("user_overview.txt", "r") as default_file:
            for line in default_file.readlines():
                newline = line.replace("\n","")
                print(newline)

    return True

def task_manager() -> bool:
    curr_user = login()

    while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        print(" ")
        if curr_user == "admin":
            menu = input('''
        Admin Menu: Select one of the following Options below:
        r  - Registering a user
        a  - Adding a task
        va - View all tasks
        vm - View my task
        gr - Generate reports
        ds - Display statistics
        e  - Exit
        : ''').lower()
        else: 
            menu = input('''
        Select one of the following Options below:
        r  - Registering a user
        a  - Adding a task
        va - View all tasks
        vm - View my task
        e  - Exit
        : ''').lower()

        if menu == 'r':
            test_r: bool = reg_user()
            
        elif menu == 'a':
            test_a: bool = add_task()

        elif menu == 'va':
            test_va: bool = view_all()

        elif menu == 'vm':
            test_vm = view_mine(curr_user)
        
        elif curr_user == "admin" and menu == "gr":
            test_gr = generate_reports()           
        
        elif menu == 'ds' and curr_user == 'admin': 
            test_ds = display_statistics(curr_user)
            
        elif menu == 'e':
            print('Goodbye!!!')
            return True
        else:
            print("You have made a wrong choice, Please try again")
        
            
if __name__ == "__main__":
    output = task_manager()