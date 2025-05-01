print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
# Prompt the user for the first choice
crossroad = input("After walking for a little while, you are at a crossroad. Where would you like to go? \n Type to choose either 'left' or 'right':\n ")
# Check to validate the first choice
if crossroad == "left" or crossroad =="Left":
  print("You come across a lake with an island in the middle.")

# Prompt the user for the second choice
  lake = input("Type to choose 'wait' to wait for a boat. Type 'swim' to swim across: \n ")
  # Check to validate the second choice
  if lake == "wait" or lake == "Wait":
    print("You make it across the lake safely. You find a house with three doors. One red, one yellow and one blue.\n")

# Prompt the user for the third choice
    door = input("Type to choose either 'red, 'yellow' or 'blue':\n ")
    # Check to validate the third choice.
    if door == "red" or door == "Red":
      print("Burned by fire. Game Over!")
    elif door == "blue" or door == "Blue":
      print("Eaten by beasts. Game Over!")
    else:
      print("You found the treasure! You Win!")

  else:
    print("You are attacked by a trout. Game Over!")

else:
  print("You fall into a hole. Game Over!")

# The code above is a simple text-based adventure game where the player makes choices to navigate through a series of scenarios. The player must choose between different paths and options, leading to various outcomes, including winning or losing the game. The game uses conditional statements to determine the player's fate based on their choices.