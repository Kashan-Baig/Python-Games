import getpass

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
while True:
    show = input("Show password while typing? (y/n): ").lower()
    if show == 'y':
        password = input("Enter a Valid Password:\n")
    else:
        password = getpass.getpass("Enter a Valid Password:\n")
    if len(password)>=8 and len(password)<=15:
        print("Valid Password")
        for i in password:
            if (i>='A' and i<='Z') and (i.isdigit() for i in password) and (i in special_chars for i in password):
                print(GREEN + "Strenght of Password --->  Strong"+ RESET)
                break
            elif ((i>='A' and i<='Z') and any(i.isdigit() for i in password)) or \
                (any(i.isdigit() for i in password) and (i in special_chars for i in password)) or \
                ((i>='A' and i<='Z') and any(i in special_chars for i in password)):
                print(YELLOW +"Strenght of Password --->  Moderate"+ RESET)
                break
            elif (i>='A' and i<='Z') or (any(i in special_chars for i in password)) or (any(i.isdigit() for i in password)) :
                print(RED + "Strenght of Password --->  Weak"+ RESET)
                break
        break
    else:
        print(RED + "Invalid Password \n Retry"+ RESET)