import random

player_win =0
computer_win = 0
while True:
    choice_player = input("Choose: Rock , Paper, Scissor: ").lower()
    print("Players Choice: ",choice_player)
    choice_computer = random.choice(["rock","paper","scissor"])
    print("Computers Choice: ",choice_computer)
    if choice_player==choice_computer:
        print("Its a tie")
    elif (choice_player=="rock" and choice_computer == "paper") or (choice_player=="scissor" and choice_computer == "rock") or \
        (choice_player=="paper" and choice_computer == "scissor"):
        print("Computer Wins")
        computer_win+=1
    elif (choice_player=="paper" and choice_computer == "rock") or (choice_player=="rock" and choice_computer == "scissor") or \
        (choice_player=="scissor" and choice_computer == "paper"):
        print("Player Wins")
        player_win+=1
    else:
        print("Invalid Choice !!")
    print("Score Card: Player {",player_win,"} Computer {",computer_win,"}")

    choice = input("Do you want to play again(Yes/No): ").lower() 
    if choice=="no":
        if(player_win>computer_win):
            print("Overall Results: Player Wins with a score of {",player_win,"}")
        elif(player_win<computer_win):
            print("Overall Results: Computer Wins with a score of {",computer_win,"}")
        else:
            print("Its a tie between both with scores of {",player_win,"}")
        print("Thanks for playing ")
        break     



