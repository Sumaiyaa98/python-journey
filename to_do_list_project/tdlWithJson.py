import json
def load_task():
    try:
        with open('myTask.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def safe_data_helper(task):
    with open('myTask.txt','w') as file:
        return json.dump(task,file,indent=4)


def add_task(task):
    mytask = input("Enter your task: ")
    task.append(mytask)
    print(f"{mytask} Task is added!")
    safe_data_helper(task)
    

def delete_task(task):
    if not task:
        print("\nNo tasks to delete!\n")
        return  # Exit the function early
    list_all_task(task)
    try:
        index = int(input("Enter the task number to be deleted: "))
        if 1 <= index <= len(task):
            del task[index - 1]
            print("Task is deleted!")
            safe_data_helper(task)
        else:
            print("Invalid index number")
    except ValueError:
        print("Please enter a valid number.")

def list_all_task(task):
    if task:
        print('Your Tasks')
        for index,tsk in enumerate(task,start=1):
            print(f"{index}- {tsk}")
    else:
        print('\n')
        print("No Task To Display!")
        print('\n')
        
    



def main():

    task = load_task()
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
        
if __name__ == '__main__':
    main()