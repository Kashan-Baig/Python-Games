import random
import time
# Number guessing game with Easy to hard level

def numguess():
     count = 0
     start_time = time.time()
     while True:
        player = int(input("Guess any number in between the range: \n "))
        count+=1
        if computer == player:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print(f"✅ Correct! You guessed the number in {count} attempts.")
            print(f"⏱️ Time taken: {total_time} seconds.")
            break
        elif computer!=player:
            if player>computer:
                print("Too High!!")
            else:
                print("Too Low!!")
        else:
            print("Your Guess is out of range")
    


level = int(input("Choose your level: 1.Easy 2.Medium 3.Hard -- choose between 1-3:\n"))
if level==1:
    print("Welcome to level -> Easy (Target 2 attempts)")
    print("Range in between 1-10")
    computer = int(random.choice(range(0,11)))
    numguess()
elif level==2:
    print("Welcome to level -> Medium ")
    print("Range in between 1-50 (Target 4 attempts)")
    computer = int(random.choice(range(0,51)))
    numguess()
elif level==3:
    print("Welcome to level -> Hard (Target 6 attempts) ")
    print("Range in between 1-100")
    computer = int(random.choice(range(0,101)))
    numguess()
else:
    print("Error in Selection")

        