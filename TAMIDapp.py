task_list=[]
task=input("Enter your task: ")
task2={
"id": len(task_list)+1,
"description": task,
"completed": False
        }
task_list.append(task2)
print(task_list)
x=2
print("Menu")
print("Enter 1 to return all tasks")
print("Enter 2 to add a new task")
print("Enter 3 to update a task")
print("Enter 4 to mark a task as complete")
print("Enter 5 to delete a task")
print("Enter 6 to quit")
while x!=6:
    x=int(input("Enter a number from menu: "))
    if x==1:
        print(task_list)
        continue
    elif x==2:
        answer="yes"
        while answer=="yes":
            task=input("Enter your task: ")
            task2={
            "id": len(task_list)+1,
            "description": task,
            "completed": False
        }
            task_list.append(task2)
            print(task_list)
            answer=input("Would you like to add another task? (yes/no) ")
    elif x==3:
        answer="yes"
        while answer=="yes":
            print(task_list)
            try:
                index = int(input("Which number task in this list would you like to change? ")) - 1
                if 0 <= index < len(task_list):
                    task = input("What would you like to change it to? ")
                    task_list[index]["description"] = task
                else:
                    print("Invalid task number! Please choose a number from the list.")
            except ValueError:
                print("Please enter a valid number.")
            answer = input("Would you like to update another task? (yes/no) ")
        print(task_list)
    elif x==4:
        print(task_list)
        try:
                index = int(input("Which number task would you like to mark complete? ")) - 1
                if 0 <= index < len(task_list):
                    task_list[index]["completed"] = True
                    break
                else:
                    print("Invalid task number! Please choose a number from the list.")
        except ValueError:
                print("Please enter a valid number.")
        print(task_list)

    elif x==5:
        print(task_list)
        try:
                index = int(input("Which number task would you like to delete? ")) - 1
                if 0 <= index < len(task_list):
                    del task_list[index]
                    break
                else:
                    print("Invalid task number! Please choose a number from the list.")
        except ValueError:
                print("Please enter a valid number.")
        print(task_list)
    else:
        print("Invalid input")

