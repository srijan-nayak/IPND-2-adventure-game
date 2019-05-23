import random
import time


def print_pause(string: str, delay=2):
    """Print a passed in string after a
    delay of passed in seconds. Default
    delay is of 2 seconds.
    """
    time.sleep(delay)
    print(string)

enemies = ["Red Dragon", "Armoured Ogre", "Ferocious Minotaur"]
enemy = random.choice(enemies)

while True:
    print_pause("You are in an empty corridor deep in a dungeon.")
    print_pause(f"You have come here to kill the {enemy}.")
    print_pause("The problem is that you broke you trusty sword "
                "while making your way till here.")
    print_pause("What do you do?")
    while True:
        print_pause("1. Give up and go back home", 1)
        print_pause("2. Continue this hopeless quest", 1)
        print_pause("Enter one of the option numbers.")
        choice = input()
        if choice == "1":
            print_pause("You exit the dungeon and go back home.")
            print_pause("GAME OVER!")
            exit()
        elif choice == 2:
            break
        else:
            print_pause("Invalid input! Enter again.")
    print_pause("Would you like to try again?")
    choice = input().lower()
    if choice != "y":
        break
