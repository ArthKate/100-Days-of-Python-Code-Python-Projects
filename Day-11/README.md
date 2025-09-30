# Blackjack Project

A command-line implementation of the classic Blackjack card game in Python.

## Features
- Deal cards to player and dealer
- Calculate hand values (Ace handling: 1 or 11)
- Player decisions: Hit or Stand
- Dealer follows standard rules (hits on 16, stands on 17)
- Win/lose/draw detection
- Basic game loop with replay option

## Game Rules
- Goal: Get hand value as close to 21 without going over
- Face cards (J, Q, K) = 10 points
- Aces = 1 or 11 points (whichever is better)
- Dealer must hit on 16 and below, stand on 17 and above
- Blackjack (21 with 2 cards) beats regular 21

## How to Play
1. Run the script
2. Cards are dealt automatically
3. Choose to 'hit' (take another card) or 'stand' (keep current hand)
4. Dealer plays after you stand or bust
5. Winner is determined and displayed