def add_task(task):
    mytask = input("Enter your task: ")
    task.append(mytask)

    print(f"{mytask} Task is added!")
    

def delete_task(task):
    if not task:
        print("\nNo tasks to delete!\n")
        return  # Exit the function early
    list_all_task(task)
    index = int(input("Enter the task number to be deleted: "))
    if 1<= index <= len(task):
        del task[index-1]
        print("Task is deleted!")
    else:
        print("Invalid index number")

def list_all_task(task):
    if task:
        print('Your Tasks')
        for index,tsk in enumerate(task,start=1):
            print(f"{index}- {tsk}")
    else:
        print('\n')
        print("No Task!")
        print('\n')
        
    


task = []

while(True):

    print('*'*43)
    
    print("To Do List | Choose an option")
    print("1- Add task")
    print("2- Delete task")
    print("3- List all tasks")
    print("4- Exit")
    print('*'*43)
    

    choice = input("Enter your choice: ")
    match(choice):
        case '1':
            add_task(task)
        case '2':
            delete_task(task)
        case '3':
            list_all_task(task)
        case '4':
            break
            
        case _:
            print("Invalid Input")
    
