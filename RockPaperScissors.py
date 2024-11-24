import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True: 

    user_input = input("Type Rock / Paper / Scissors or q to quit  \n").lower()
    if user_input == "q" : 
        break

    if user_input not in options: 
        print("invalid input")
        continue
    random_number = random.randint(0,2)
    #0 : rock , 1: paper, 2: scissors
    print()
    computer_choice = options[random_number]
    print("Computer's Choice: ", computer_choice)
    if user_input == "rock" and computer_choice == "scissors": 
        print("You Won...!")
        user_wins += 1
        

    elif user_input == "paper" and computer_choice == "rock": 
        print("You Won...!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_choice == "paper": 
        print("You Won...!")
        user_wins += 1
        

    elif user_input == computer_choice : 
        print("Nobody Wins, Tie.")

    else: 
        print("Computer Wins...!")
        computer_wins+=1
    
print("User Score: " + str(user_wins) )
print("Computer Score : " + str(computer_wins))
if computer_wins > user_wins : 
    print("Computer Won the Match....!")
else: 
    print("User Won the Match....!")



