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
        print_pause("Enter one of the option numbers.")
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
            print_pause("You take a deep breath before you open the "
                        "black door.")
            print_pause("You know what's beyond this door.")
            print_pause("You open the door.")
            print_pause(f"You find the {enemy} in the room.")
            while True:
                print_pause("What do you do?")
                option_count = 0
                if writing_utensil in items:
                    option_count += 1
                    print_pause(f"{option_count}. Fight him with your pen", 1)
                if "deathnote" in items:
                    option_count += 1
                    print_pause(f"{option_count}. Ask for his autograph", 1)
                option_count += 1
                print_pause(f"{option_count}. Run back to the corridor.", 1)
                print_pause("Enter one of the option numbers.", 0)
                choice = input()
                if option_count == 3:
                    if choice == "1":
                        print_pause("You uncap your pen that you just found.")
                        print_pause(f"You rush towards the {enemy} swinging "
                                    "your pen.")
                        print_pause("But you never stood a chance with your "
                                    "pen.")
                        print_pause(f"The {enemy} renders you unfit for "
                                    "battle with a single attack.")
                        repeatCorridorChoice = False
                        break
                    elif choice == "2":
                        print_pause("You gather all your courage and ask "
                                    f"the {enemy} for his autograph.")
                        print_pause(f"Agreeing to your request, the {enemy} "
                                    "takes your DEATHNOTE and "
                                    f"your {writing_utensil} for signing.")
                        print_pause("While blushing. A lot.")
                        print_pause("He signs his name in the DEATHNOTE.")
                        print_pause("You take back the DEATHNOTE and the pen.")
                        print_pause(f"The {enemy} suddenly has a heart attack "
                                    "10 seconds after signing his name.")
                        print_pause(f"The {enemy} is dead!")
                        print_pause("Looks like the DEATHNOTE worked.")
                        print_pause("Congrats!")
                        print_pause(f"You have killed the {enemy}!")
                        print_pause("You won!")
                        repeatCorridorChoice = False
                        break
                    elif choice == "3":
                        print_pause("You run back to the corridor.")
                        print_pause(f"Looks like the {enemy} has not "
                                    "followed you.")
                        break
                    else:
                        print_pause("Invalid input! Enter again.")
                elif option_count == 2:
                    if choice == "1" and writing_utensil in items:
                        print_pause("You uncap your pen that you just found.")
                        print_pause(f"You rush towards the {enemy} swinging "
                                    "your pen.")
                        print_pause("But you never stood a chance with your "
                                    "pen.")
                        print_pause(f"The {enemy} renders you unfit for "
                                    "battle with a single attack.")
                        repeatCorridorChoice = False
                        break
                    elif choice == "1" and "deathnote" in items:
                        print_pause("You gather all your courage and ask "
                                    f"the {enemy} for his autograph.")
                        print_pause(f"But the {enemy} is annoyed that you "
                                    "don't have a writing utensil!")
                        print_pause(f"The {enemy} renders you unfit for "
                                    "battle with a single attack.")
                        repeatCorridorChoice = False
                        break
                    elif choice == "2":
                        print_pause("You run back to the corridor.")
                        print_pause(f"Looks like the {enemy} has not "
                                    "followed you.")
                        break
                    else:
                        print_pause("Invalid input! Enter again.")
                elif option_count == 1:
                    if choice == "1":
                        print_pause("You run back to the corridor.")
                        print_pause(f"Looks like the {enemy} has not "
                                    "followed you.")
                        break
                    else:
                        print_pause("Invalid input! Enter again.")
        else:
            print_pause("Invalid input! Enter again.")
    print_pause("Would you like to try again?")
    choice = input().lower()
    if choice != "y":
        break
