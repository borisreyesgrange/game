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
    return text_color(color, text(1, 8))


# -- SELECT CLASS -- #

def select_class():
    class_list = ["Binary Mage", "Encryption Warrior", "Algorithm Hunter"]
    color_list = ["blue", "yellow", "magenta"]

    chosen_class = ""
    while chosen_class not in ("1", "2", "3"):
        print("Choose the class of your hero:\n")
        print(text_color(color_list[0], "1) "+class_list[0]), text_color(color_list[1], "\n2) "+class_list[1]),
              text_color(color_list[2], "\n3) "+class_list[2]))
        chosen_class = input("\nEnter your option number: ")
        if chosen_class not in ("1", "2", "3"):
            print("Invalid option, you must enter the number... try again\n")
            time.sleep(1)
    return [class_list[int(chosen_class)-1], color_list[int(chosen_class)-1]]


# -- NAME THE  HERO --#

def hero_name(chosen_class, color):
    creation_confirm = ""

    print("\nNow you must name your hero")
    chosen_name = input("Write the name of your character: ")

    while creation_confirm != "yes":
        print("\nYou choose the class", text_color(color, chosen_class), "for your new hero named", text_color(color, chosen_name))
        creation_confirm = input("Type"+text_color(color, "'yes'")+"if you are sure about this to begin ")
        if creation_confirm != "yes":
            print("\nInvalid option, you must write", text_color(color, "yes"), "... lets start again\n")
            time.sleep(1)
            return False
    return chosen_name

# -- CREATING THE HERO -- #


def configure_hero(chosen_class):
    hero_class = chosen_class.rsplit(" ", 1)[1]
    return hero_class


