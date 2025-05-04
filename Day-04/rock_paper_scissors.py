# Rock Paper Scissors Game

# This is a simple classic Rock Paper Scissors game where the user plays against the computer.
# The user can choose rock, paper, or scissors, and the computer randomly chooses one of the three options.

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Define the options
option = [rock, paper, scissors]


# Get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Get computer's choice
computer_choice = random.choice(option)

if user_choice == 0:
  print(rock)
  print(f"Computer chose: \n{computer_choice}\n")
  if computer_choice == rock:
    print("it's a draw")
  elif computer_choice == paper:
    print("You lose")
  else:
    print("You win")
elif user_choice == 1:
  print(paper)
  print(f"Computer chose:\n {computer_choice}\n")
  if computer_choice == paper:
    print("it's a draw")
  elif computer_choice == rock:
    print("You win")
  else:
    print("You lose")
elif user_choice == 2:
  print(scissors)
  print(f"Computer chose:\n {computer_choice}\n")
  if computer_choice == scissors:
    print("It's a draw")
  elif computer_choice == paper:
    print("You win")
  else:
    print("You lose")
else:
  print("Invalid choice. Please try again.")