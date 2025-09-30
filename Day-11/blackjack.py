from art import logo
from random import choice

# Blackjack game project playing against the computer
print(logo)

#Deal cards to player and computer cards in turns
def deal_card(hand, deck):
  for i in range(2):
    card = choice(deck)
    hand.append(card)
    deck.remove(card)
  return hand

# handle ace logic to calculate score
def calculate_score(hand):
  '''calculate the best possible score for a hand, handling ace logic.'''
  # adding up all cards
  score = sum(hand)
  num_aces = hand.count(11) # counting the aces in our hand
  while score > 21 and num_aces > 0:
    score -= 10 # convert ace from 11 to 1
    num_aces -= 1
  return score

#play
def play_blackjack():
  #create fresh deck for each game
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  #initialize local variables
  player= list()
  computer = []
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if play == 'y':
    
    # deal cards to player
    player_hand = deal_card(player, deck)
    player_score = calculate_score(player_hand)
    
    # deal cards to computer
    computer_hand  = deal_card(computer, deck)
    computer_score = calculate_score(computer_hand)
    
    print(f"Your cards: {player_hand}, current score: {player_score}")
    #computer's turn
    print(f"Computer's first card: {computer_hand[0]}")

    continue_playing = True

    while continue_playing:
      another_card = input("Type 'y' to hit and get another card, type 'n' to stand: ").lower()
      # Computer should only draw cards based on blackjack rules (typically when < 17)

      if another_card == "y":
        # player draws a card
        card = choice(deck)
        player_hand.append(card)
        deck.remove(card)
        player_score = calculate_score(player_hand)

        # check for player bust
        if player_score > 21:
          print(f"Your final hand: {player_hand}, final score : {player_score}")
          print("You went over. You lose!")
          continue_playing = False
          continue

        print(f"Your cards: {player_hand}, current score: {player_score}")


      elif another_card == "n": # player doesn't wish to be dealt another card

        while computer_score < 17:
          card = choice(deck)
          computer_hand.append(card)
          deck.remove(card)
          computer_score = calculate_score(computer_hand)

        # Final game resolution
        print(f"Your final hand: {player_hand}, final score : {player_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        # Determine winner
        if computer_score > 21:
          print("Computer went over. You win!")
        elif player_score > computer_score:
          print("You win!")
        elif computer_score > player_score:
          print("You lose!")
        else:
          print("It's a draw!")

        continue_playing = False
  else:
    print("You welcome to play next time, Good bye!")


play_blackjack()


























