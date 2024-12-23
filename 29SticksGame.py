def play_sticks_game():
    print("Welcome to the Sticks Game!")
 


    total_sticks = 16
    current_player = 1 


    while total_sticks > 0:
        print(f"Sticks remaining: {total_sticks}")
        print(f"Player {current_player}, how many sticks will you take (1-3)?")
        sticks_taken = input()
        
        if not sticks_taken.isdigit():
            print("Invalid input! Please enter a number between 1 and 3.")
            continue
        
        sticks_taken = int(sticks_taken)


        if sticks_taken < 1 or sticks_taken > 3:
            print("Invalid input! You can only take 1, 2, or 3 sticks.")
            continue
        if sticks_taken > total_sticks:
            print(f"Invalid input! Only {total_sticks} sticks remaining.")
            continue


        total_sticks -= sticks_taken


        if total_sticks == 0:
            print(f"Player {current_player} loses the game!")
            break


        current_player = 2 if current_player == 1 else 1


play_sticks_game()