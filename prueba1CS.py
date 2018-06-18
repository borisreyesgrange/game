import time
import random

points_p1 = 50
points_p2 = 50

print("Welcome to the Random Battle")
time.sleep(1)
print("Enter the name of the players:")

player1 = input("Player 1:")
player2 = input("Player 2:")

print("Today's battle:", player1, "v/s", player2)
print("Begin!!")
time.sleep(2)

while points_p1 < 100 and points_p2 < 100:
    print("Chosing....")
    time.sleep(1)
    player_hit = random.randint(1, 2)

    if player_hit == 1:
        play = random.randint(10,40)
        points_p1 = points_p1 + play
        print(player1, "You have luck!, you won", play, "points")
        points_p2 = points_p2 - play

    if player_hit == 2:
        play = random.randint(10,40)
        points_p2 = points_p2 + play
        print(player2, "You have luck!, you won", play, "points")
        points_p1 = points_p1 - play

    print("Score:", player1, "has: ", points_p1, "points")
    print("Score:", player2, "has: ", points_p2, "points")
    input("Press enter to continue\n")

if points_p1 > 100:
    print("Great Battle, congratulations to:", player1)
elif points_p2 > 100:
    print("Good Battle, congratulations to:", player2)
else:
    print("How do I get Here??")

print("GAME OVER")
