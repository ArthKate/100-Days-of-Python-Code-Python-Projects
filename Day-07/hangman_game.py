import random
from hangman_words import word_list
from hangman_art import logo, stages

secret_word = random.choice(word_list) # Randomly select a word from the list
display = ["_"] * len(secret_word)  # Create a placeholder for the word
hint = "".join(display)
lives = 6  # Number of lives the player has.
print(logo)  # Display the hangman logo
print("\n")
print(f" Guess the secret word: {''.join(hint)}")  # Show the initial hint with underscores
print()
print(f"========= You have {lives} lives =========")
print()
print("-------------------------------------------")

#track game state
is_game_over = False
guessed_letters = set()

while not is_game_over:
    guess = input("Guess a letter: ").lower()  # Prompt the player to guess a letter
    print()
    if guess in secret_word:
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
        for i, letter in enumerate(secret_word):
            if guess == letter:
                guessed_letters.add(guess)
                # Reveal the correctly guessed letter in the hint
                display[i] = letter
                hint = "".join(display)
                print(hint)
                continue
    else:
        lives -= 1
        print(f"invalid input, you lose a {lives}/6 lives left")
        print(hint)

    

    # determine win/lose
    if lives == 0:
        print("*************************************")
        print("You lose!")
        print(f"The secret word was : {secret_word}")
        print("*************************************")
        is_game_over = True

    if "_" not in hint:
        print("*************************************")
        print("You win!, Thumbs up")
        print(f"You guessed the secret word :{secret_word} ")
        print("*************************************")
        is_game_over = True
        
