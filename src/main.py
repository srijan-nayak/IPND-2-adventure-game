import random
import time


def print_pause(string: str, delay=2)->None:
    """Print a passed in string after a
    delay of passed in seconds. Default
    delay is of 2 seconds.
    """
    print(string)
    time.sleep(delay)


enemies = ["Red Dragon", "Armoured Ogre", "Ferocious Minotaur"]
enemy = random.choice(enemies)
writing_utensils = ["pen", "pencil", "marker"]
writing_utensil = random.choice(writing_utensils)
choice = ""
items = []

while True:
    print_pause("You are in an empty corridor deep in a dungeon.")
    print_pause(f"You have come here to kill the {enemy}.")
    print_pause("The problem is that you broke you trusty sword "
                "while making your way till here.")
    while True:
        print_pause("What do you do?")
        print_pause("1. Give up and go back home", 1)
        print_pause("2. Continue this hopeless quest", 1)
        print_pause("Enter one of the option numbers.", 0)
        choice = input()
        if choice == "1":
            print_pause("You exit the dungeon and go back home.")
            print_pause("GAME OVER!")
            exit()
        elif choice == "2":
            break
        else:
            print_pause("Invalid input! Enter again.")
    print_pause("You spot three doors in the corridor.")
    repeatCorridorChoice = True
    while repeatCorridorChoice:
        print_pause("Where would you like to go?")
        print_pause("1. Go to the room with the green room on the left", 1)
        print_pause("2. Go to the room with the blue door on the right", 1)
        print_pause("3. Go to the room with the black door at the end\n"
                    "of the corridor")
        print_pause("Enter one of the option numbers.")
        choice = input()
        if choice == "1":
            print_pause("You enter the room with the green door.")
            if "deathnote" not in items:
                print_pause("You find a black notebook lying on the ground.")
                print_pause("The notebook has DEATHNOTE written on it.")
                print_pause("It has some instructions written in it.")
                print_pause("Looks like if you write someone's name, whose")
                print_pause("face you have seen, in the DEATHNOTE, that")
                print_pause("person will die in 10 seconds due to a heart")
                print_pause("attack.")
                items.append("deathnote")
                print_pause("You take the DEATHNOTE.")
            else:
                print_pause("There's nothing here.")
            print_pause("You leave the room.")
        elif choice == "2":
            print_pause("You enter the room with the blue door.")
            if writing_utensil not in items:
                print_pause(f"You find a {writing_utensil} lying on "
                            "the ground.")
                items.append(writing_utensil)
                print_pause(f"You take the {writing_utensil}.")
            else:
                print_pause("There is nothing here.")
            print_pause("You leave the room.")
        elif choice == "3":
            pass
        else:
            print_pause("Invalid input! Enter again.")
    print_pause("Would you like to try again?")
    choice = input().lower()
    if choice != "y":
        break
