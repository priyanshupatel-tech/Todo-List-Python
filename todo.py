import json 
 
def save_task(task):
    with open("todo.json","w")as file:
        json.dump(task,file,indent=4)

def load_task():
    try:
        with open("todo.json","r") as file:
            return json.load(file)
    except:
        return []
    
def task_header():
    print(f"{'Task Name':<20}{'Due Date':<25}{'Task Priority':<26}Task Status")
    print("-"*85)


def menu():
    print("="*35,"To Do List Menu","="*35)
    print("1.Add Task")
    print("2.View Task")
    print("3.Done Task")
    print("4.Pending Task")
    print("5.High Priority Task")
    print("6.Low Priority Task")
    print("7.Medium Priority Task")
    print("8.Delete Task")
    print("10.Exit")
    
def add_task():
    task=load_task()
    name=input("Enter Task Name=").title()
    for tasks in task:
        if tasks['Name']==name:
            print("-"*85)
            return print("This task is allready Exist!") 
    else:        
        print("Enter Due date of Task=")
        try:
            d=int(input("Enter Day="))
            if d<=31:
                pass
            else:
                print("-"*85)
                print("Please Give a Valid Day")
                return 
            m=int(input("Enter Month="))
            if m<=12 and m>0:
                pass
            else:
                print("-"*85)
                print("Please Give a valid month")
                return
            y=int(input("Enter Year="))
            if y>=2026:
                pass
            else:
                print("-"*85)
                print("Please Give Upcoming Year")
                return
        except:
            print("-"*85)
            print("Please give only numeric Value")
            return
        date=(f"{d}/{m}/{y}")
        print("Task Priority---\nLow=1\nHigh=2\nMedium=3")
        
        try:
            priority=int(input("Enter Task's Priority="))
            if priority<=3:
                if priority==1:
                    priority="Low"
                elif priority==2:
                    priority="High"
                else:
                    priority="Medium"
            else:
                print("-"*85)
                print("Please Give a valid priority number")
                return
        except:
            print("Please give only number")
        print("Task Status---\nDone=1\nPending=2")
        try:
            status=int(input("Enter your Task Status="))
            if status<=2 and status>0:
                if status==2:
                    status="Pending"
                else:
                    status="Done"
            else:
                print("-"*85)
                print("Please Give a valid status number")
                return
        except:
            print("-"*85)
            print("Please give only number")
        task.append(
            {
                "Name":name,
                "Date":date,
                "Priority":priority,
                "Status":status
            }
        )
        save_task(task)
        print("-"*85,"\nTask Added Suceesfully!")
        return task

def view_task():
    task_header()
    task=load_task()
    for tasks in task:
        print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")

def done_task():
    task=load_task()
    task_header()
    for tasks in task:
        if tasks['Status']=="Done":
            print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")

def pending_task():
    task=load_task()
    task_header()
    for tasks in task:
        if tasks['Status']=="Pending":
            print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")

def high_task():
    task=load_task()
    task_header()
    for tasks in task:
        if tasks['Priority']=="High":
            print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")

def low_task():
    task=load_task()
    task_header()
    for tasks in task:
        if tasks['Priority']=="Low":
            print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")

def mid_task():
    task=load_task()
    task_header()
    for tasks in task:
        if tasks['Priority']=="Medium":
            print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")

def delete_task():
    task=load_task()
    task_header()
    for tasks in task:
        print(f"{tasks['Name']:<20}{tasks['Date']:<25}{tasks['Priority']:<26}{tasks['Status']}")
    rem=input("Enter Task name you want to delete=").title()
    try:
        for tasks in task[:]:
            if tasks.get("Name") == rem:
                task.remove(tasks)
                print("Task Removed Succesfully!")
    except:
        print("task Dosn't  exist!")
    save_task(task)
    return task



while True:
        menu()
        choice=int(input("Enter Your Choice Number="))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            done_task()
        elif choice==4:
            pending_task()
        elif choice==5:
            high_task()
        elif choice==6:
            low_task()
        elif choice==7:
            mid_task()
        elif choice==8:
            delete_task()
        elif choice==10:
            exit()

        
