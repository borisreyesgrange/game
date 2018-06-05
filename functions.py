import random
from styles import *

# -- GLOBAL VARIABLES --#
color_list = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
characters =["Binary Mage", "Hexadecimal Warlock", "Encryption Destroyer"]

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


# -- Select Character -- #

def select_character(game_color):
    selected_character = ""
    while selected_character not in ("1", "2", "3"):
        print(text_color(game_color, "Choose your character:\n"))
        print(text_color("green", "1) "+characters[0]), text_color("blue", "\n2) "+characters[1]),
              text_color("yellow", "\n3) "+characters[2]))
        selected_character = input()

