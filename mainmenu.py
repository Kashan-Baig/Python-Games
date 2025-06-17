import os

def showmenu():
    print("\n🎮 PYTHON MINI PROJECT HUB")
    print("1. Number Guessing Game")
    print("2. Rock Paper Scissors")
    print("3. Password Strength Checker")
    print("4. To-Do List Manager")
    print("5. Exit")

while True:
    showmenu()
    choice = int(input("Enter Your Choice From The Following Above: \n"))

    if choice == 1:
        os.system("python number_guess.py")
    elif choice == 2:
        os.system("python rock_paper_scissors.py")
    elif choice == 3:
        os.system("python password_checker.py")
    elif choice == 4:
        os.system("python to_do_list.py")
    elif choice == 5:
        print("👋 Exiting the Mini Project Hub. Goodbye!")
        break
    else:
        print("❗ Invalid choice. Please select a valid option.")