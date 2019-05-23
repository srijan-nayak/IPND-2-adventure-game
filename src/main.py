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
