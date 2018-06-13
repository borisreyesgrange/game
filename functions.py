import random
import time
from styles import *
from classes import *

# -- EXTRACT TEXTS FROM FILE-- #


def text(begin, end):
    lines = ""
    with open("texts.txt") as text:
        lines_list = text.readlines()
        for line in range(begin-1, end):
            lines = lines+str(lines_list[line])
        return lines

# -- PRINT TITLE OF THE GAME -- #


def title(color):
    return tc(color, text(1, 8))


# -- SELECT CLASS -- #

def select_class():
    class_list = ["Binary Mage", "Encrypted Warrior", "Algorithm Hunter"]
    color_list = ["blue", "yellow", "magenta"]

    chosen_class = ""
    while chosen_class not in ("1", "2", "3"):
        print("Choose the class of your hero:\n")
        print(tc(color_list[0], "1) "+class_list[0]), tc(color_list[1], "\n2) "+class_list[1]),
              tc(color_list[2], "\n3) "+class_list[2]))
        chosen_class = input("\nEnter your option number: ")
        if chosen_class not in ("1", "2", "3"):
            print("Invalid option, you must enter the number... try again\n")
            time.sleep(1)
    return class_list[int(chosen_class)-1]


# -- ASSIGN COLOR TO A HERO -- #


def assign_color(chosen_class):
    color_list = ["blue", "yellow", "magenta"]

    if chosen_class == "Binary Mage":
        return color_list[0]

    if chosen_class == "Encrypted Warrior":
        return color_list[1]

    if chosen_class == "Algorithm Hunter":
        return color_list[2]


# -- NAME THE  HERO --#

def hero_name(chosen_class, color):
    creation_confirm = ""

    print("\nNow you must name your hero")
    chosen_name = input("Write the name of your character: ")

    while creation_confirm != "yes":
        print("\nYou choose the class", tc(color, chosen_class), "for your new hero named", tc(color, chosen_name))
        creation_confirm = input("Type"+tc(color, "'yes'")+"if you are sure about this to begin ")
        if creation_confirm != "yes":
            print("\nInvalid option, you must write", tc(color, "yes"), "... lets start again\n")
            time.sleep(1)
            return False
    return chosen_name


