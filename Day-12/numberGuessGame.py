import random
import art
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while not difficulty_level.isalpha():
  print("Invalid input, please choose either 'easy or 'hard': ")
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


num = random.randrange(1, 100)

if difficulty_level == 'easy':
  chances = 10
else:
  chances = 5


while  chances > 0:
  print(f"You have {chances} attempts remaining to guess the number.")
  guess = input("Make a guess: ")

  while not guess.isdigit():
    print("Invalid input, please type a number")
    guess = input("Make a guess: ")

  guess = int(guess)

  if guess > num:
    print("Too high")
    chances -= 1
    if chances == 0:
      print("Game Over!")
      print("\n")
      print("Refresh the page to play again")
      break
    continue
  elif guess < num:
    print("Too low.")
    chances -= 1
    if chances == 0:
      print("Game Over!")
      print("\n")
      print("Refresh the page to play again")
      break
    continue
  else:
    print(f"You got  it! The answer was {guess}")
    print("\n")
    print("Refresh the page to play again")
    break




