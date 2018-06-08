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

    # CHOSEN A CLASS
    class_config = select_class()
    chosen_class = class_config[0]
    color = class_config[1]

    # DEFINE THE NAME
    chosen_name = hero_name(chosen_class, color)

# HERO CREATION
hero_class = configure_hero(chosen_class)

if hero_class == "Mage":
    hero = Mage(chosen_name)
elif hero_class == "Warrior":
    hero = Warrior(chosen_name)
elif hero_class == "Hunter":
    hero = Hunter(chosen_name)

print("\nWelcome", text_color(color, hero.name), "the", text_color(color, hero.className))

