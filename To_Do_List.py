

def viewtask():
    f = open("Task.txt","r")
    content = f.read()
    if content:
         print("\n📋 Your Tasks:\n" + content)
    else:
        print("\n✅ No tasks found.")
    f.close()


def addtask():
    with open("Task.txt", "a") as f:
        content = input("Write any task:\n")
        f.write(content+"\n")

def delete():
    index = int(input("Enter the task number to delete: \n"))-1
    f = open("Task.txt","r")
    content = f.readlines()
    if 0<=index<=len(content):
        remove = content.pop(index)
        print(f"❌ Task removed: {remove.strip()}")
        with open("Task.txt", "w") as f:
            f.writelines(content)
    else:
        print("⚠️ Invalid task number.")

        


while True:
    print("\n📋 TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = int(input("Enter Your Choice: \n"))

    if choice==1:
        viewtask()
    elif choice==2:
        addtask()
    elif choice==3:
        delete()
    elif choice==4:
        print("Good Bye")
        break
    else:
        print("Invalid choice. Try again.")

    
        