from classes import *
from styles import *
from functions import *
import time

chosen_name = False
chosen_class = ""
color = ""
hero = None

while not chosen_name:

    # SHOWING TITLE
    print(title("cyan"))

    # CHOOSE A CLASS
    chosen_class = select_class()

    # ASSIGN COLOR DEPENDING OF THE CLASS
    color = assign_color(chosen_class)

    # DEFINE THE NAME
    chosen_name = hero_name(chosen_class, color)

# HERO CREATION

if chosen_class == "Binary Mage":
    hero = Mage(chosen_name)
elif chosen_class == "Encrypted Warrior":
    hero = Warrior(chosen_name)
elif chosen_class == "Algorithm Hunter":
    hero = Hunter(chosen_name)

print("\nWelcome", tc(color, hero.name), "the", tc(color, hero.className))

