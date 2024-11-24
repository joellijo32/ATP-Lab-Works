name = input("Enter Your Name: ")
print("\n")
print("Hi", name + ", would you like to play this game...?  \n")
whether_need_to_play_the_game = input().lower()
if whether_need_to_play_the_game == "no" : 
    print("Oh, You're too childish to not play this game..! \n")
    print("Bye.")
else: 
    print("Yeah..! \n")
    print("Welcome to the Adventure,",name,"!")
    answer = input("Your on a plain street lonely in the midnight, not aware of the route. \nYou encoutered a split of the road, Which way do you go..? Left or Right...? \n").lower()
    if answer == "left": 
        print("Bruh, It Was the Castle of Dedsha, Who commited suicide there ,Years ago...")
        print("You are Hearing some Wierd Noises of somebody uttering your name, someone crying, What will you do...?\n")
        print("Run or Adventure...?\n")
        run_or_adventure = input().lower()
        if run_or_adventure == "adventure": 
            print("Oh GOD, You Entered into the Mouth of Dedsha....Bruh You got Killed.")
            print("Well That Was a Bad Ending, " + name)
            print("bruh")
        else: 
            print("Well, You was bitten by a Vampire and got killed , bruh...!")
    else: 
        print("Ohh...!, You Reached your Home, " + name)
        print("You Can now take some sleep after the long journey...")
        print("Bruh, WTF is this...!")