import time
from functions import *
graphics_color = random.choice(["red", "green", "yellow", "blue", "cyan"])
game_color = "magenta"

print(title(graphics_color))
input(text_color(game_color, "Press enter when you are ready"))
select_character(game_color)

#print_title()

#print(red("Mi texto"))

#print(text_color("cyan", "Texto a colorear"))

#print(text_color("red", title()))

#print(text_delay(8, 12, 4))
