import random
import time


def print_pause(string: str,
                delay=2) -> None:
    """Give a pause of passed in seconds after
    printing a passed in string. Default delay
    is of 2 seconds.
    """
    print(string)
    time.sleep(delay)


def enter_green_door(items: list,
                     writing_utensil: str,
                     enemy: str) -> None:
    """Handles the green door room experience.
    """
    print_pause("You enter the room with the green door.")
    if "deathnote" not in items:
        print_pause("You find a black notebook lying on the ground.")
        print_pause("The notebook has DEATHNOTE written on it.")
        print_pause("It has some instructions written in it.")
        print_pause("Looks like if you write someone's name, whose", 1)
        print_pause("face you have seen, in the DEATHNOTE, that", 1)
        print_pause("person will die in 10 seconds due to a heart", 1)
        print_pause("attack.", 1)
        items.append("deathnote")
        print_pause("You take the DEATHNOTE.")
    else:
        print_pause("There's nothing here.")
    print_pause("You leave the room.")
    corridor_choice(items, writing_utensil, enemy)


def enter_blue_door(items: list,
                    writing_utensil: str,
                    enemy: str) -> None:
    """Handles the blue door room experience.
    """
    print_pause("You enter the room with the blue door.")
    if writing_utensil not in items:
        print_pause(f"You find a {writing_utensil} lying on "
                    "the ground.")
        items.append(writing_utensil)
        print_pause(f"You take the {writing_utensil}.")
    else:
        print_pause("There is nothing here.")
    print_pause("You leave the room.")
    corridor_choice(items, writing_utensil, enemy)


def handle_all_items_choice(choice: str,
                            items: list,
                            writing_utensil: str,
                            enemy: str) -> None:
    """Choice handler for black door room when
    player has collected all items.
    """
    if choice == "1":
        print_pause(f"You take the {writing_utensil} that you just found.")
        print_pause(f"You rush towards the {enemy} swinging "
                    f"your {writing_utensil}.")
        print_pause("But you never stood a chance with your "
                    f"{writing_utensil}.")
        print_pause(f"The {enemy} renders you unfit for "
                    "battle with a single attack.")
    elif choice == "2":
        print_pause("You gather all your courage and ask "
                    f"the {enemy} for his autograph.")
        print_pause(f"Agreeing to your request, the {enemy} "
                    "takes your DEATHNOTE and "
                    f"your {writing_utensil} for signing.")
        print_pause("While blushing. A lot.")
        print_pause("He signs his name in the DEATHNOTE.")
        print_pause(f"You take back the DEATHNOTE and the {writing_utensil}.")
        print_pause(f"The {enemy} suddenly has a heart attack "
                    "10 seconds after signing his name.")
        print_pause(f"The {enemy} is dead!")
        print_pause("Looks like the DEATHNOTE worked.")
        print_pause("Congrats!")
        print_pause(f"You have killed the {enemy}!")
        print_pause("You won!")
    elif choice == "3":
        print_pause("You run back to the corridor.")
        print_pause(f"Looks like the {enemy} has not "
                    "followed you.")
        corridor_choice(items, writing_utensil, enemy)
    else:
        print_pause("Invalid input! Enter again.")
        black_door_choice(items, writing_utensil, enemy)


def handle_1_item_choice(choice: str,
                         items: list,
                         writing_utensil: str,
                         enemy: str) -> None:
    """Choice handler for black door room when
    player has found only one of the items.
    """
    if choice == "1" and writing_utensil in items:
        print_pause(f"You take the {writing_utensil} that you just found.")
        print_pause(f"You rush towards the {enemy} swinging "
                    f"your {writing_utensil}.")
        print_pause("But you never stood a chance with your "
                    f"{writing_utensil}.")
        print_pause(f"The {enemy} renders you unfit for "
                    "battle with a single attack.")
    elif choice == "1" and "deathnote" in items:
        print_pause("You gather all your courage and ask "
                    f"the {enemy} for his autograph.")
        print_pause(f"But the {enemy} is annoyed that you "
                    "don't have a writing utensil!")
        print_pause(f"The {enemy} renders you unfit for "
                    "battle with a single attack.")
    elif choice == "2":
        print_pause("You run back to the corridor.")
        print_pause(f"Looks like the {enemy} has not "
                    "followed you.")
        corridor_choice(items, writing_utensil, enemy)
    else:
        print_pause("Invalid input! Enter again.")
        black_door_choice(items, writing_utensil, enemy)


def handle_no_item_choice(choice: str,
                          items: list,
                          writing_utensil: str,
                          enemy: str) -> None:
    """Choice handler for black door room when
    player has found none of the items.
    """
    if choice == "1":
        print_pause("You run back to the corridor.")
        print_pause(f"Looks like the {enemy} has not "
                    "followed you.")
        corridor_choice(items, writing_utensil, enemy)
    else:
        print_pause("Invalid input! Enter again.")
        black_door_choice(items, writing_utensil, enemy)


def black_door_choice(items: list,
                      writing_utensil: str,
                      enemy: str) -> None:
    """Choice presenter for the black door room.
    """
    print_pause("What do you do?")
    option_count = 0
    if writing_utensil in items:
        option_count += 1
        print_pause(f"{option_count}. Fight him with the {writing_utensil}", 1)
    if "deathnote" in items:
        option_count += 1
        print_pause(f"{option_count}. Ask for his autograph", 1)
    option_count += 1
    print_pause(f"{option_count}. Run back to the corridor.", 1)
    print_pause("Enter one of the option numbers.", 0)
    choice = input()
    if option_count == 3:
        handle_all_items_choice(choice, items, writing_utensil, enemy)
    elif option_count == 2:
        handle_1_item_choice(choice, items, writing_utensil, enemy)
    elif option_count == 1:
        handle_no_item_choice(choice, items, writing_utensil, enemy)


def enter_black_door(items: list,
                     writing_utensil: str,
                     enemy: str) -> None:
    """Intro for the black door room choice scenario.
    """
    print_pause("You take a deep breath before you open the "
                "black door.")
    print_pause("You know what's beyond this door.")
    print_pause("You open the door.")
    print_pause(f"You find the {enemy} in the room.")
    black_door_choice(items, writing_utensil, enemy)


def corridor_choice(items: list,
                    writing_utensil: str,
                    enemy: str) -> None:
    """Choice presenter and handler for the corridor.
    """
    print_pause("Where would you like to go?")
    print_pause("1. Go to the room with the green door on the left", 1)
    print_pause("2. Go to the room with the blue door on the right", 1)
    print_pause("3. Go to the room with the black door at the end of the "
                "corridor", 1)
    print_pause("Enter one of the option numbers.", 0)
    choice = input()
    if choice == "1":
        enter_green_door(items, writing_utensil, enemy)
    elif choice == "2":
        enter_blue_door(items, writing_utensil, enemy)
    elif choice == "3":
        enter_black_door(items, writing_utensil, enemy)
    else:
        print_pause("Invalid input! Enter again.")
        corridor_choice(items, writing_utensil, enemy)


def start_adventure() -> None:
    """Starts the game.
    """
    # Enemy and writing_utensil is selected on random each time the game
    # starts or restarts.
    enemy = random.choice(["Red Dragon",
                           "Armoured Ogre",
                           "Ferocious Minotaur"])
    writing_utensil = random.choice(["pen",
                                     "pencil",
                                     "marker"])
    items = []  # Empty inventory for the player.
    print_pause("You are in an empty corridor deep in a dungeon.")
    print_pause(f"You have come here to kill the {enemy}.")
    print_pause("The problem is that you broke you trusty sword "
                "while making your way till here.")
    print_pause("But still you contniue on this hopeless quest.")
    print_pause("You spot three doors in the corridor.")
    corridor_choice(items, writing_utensil, enemy)
    print_pause("Would you like to try again ? [Y/n]")
    choice = input().lower()
    if choice == "y":  # Game terminates if input is anything other than Y/y.
        start_adventure()


start_adventure()
