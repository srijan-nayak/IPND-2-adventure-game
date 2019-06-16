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
    print_pause("But still you contniue on this hopeless quest.")
    print_pause("Would you like to try again?")
    choice = input().lower()
    if choice != "y":
        break
