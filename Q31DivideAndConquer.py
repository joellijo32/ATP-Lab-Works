import random

def roll_die_visual():
    # Simulate rolling a six-sided die
    number = random.randint(1, 6)
    
    # ASCII art for die faces
    dice_faces = {
        1: (
            "+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"
        ),
        2: (
            "+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"
        ),
        3: (
            "+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"
        ),
        4: (
            "+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"
        ),
        5: (
            "+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"
        ),
        6: (
            "+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"
        )
    }
    
    # Display the rolled number and its die face
    print(f"You rolled a {number}!")
    print("\n".join(dice_faces[number]))

# Simulate and display the die roll visually
roll_die_visual()
