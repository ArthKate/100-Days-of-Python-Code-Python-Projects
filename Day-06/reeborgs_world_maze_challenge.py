#REEBORG''S WORLD MAZE CHALLENGE 
# This is a simple maze challenge where Reeborg has to find the exit.
# The maze is represented as a grid where 0 is a free cell and 1 is a wall.
# The goal is to navigate Reeborg from the starting position to the exit.
# # Code in the solution follows the parameters (world conditions set in the gaming environment):

# Turn right function
def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():
    
    if right_is_clear():
        library.turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
