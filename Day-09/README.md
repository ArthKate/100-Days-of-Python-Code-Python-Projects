# Blind Auction Project

This project implements a simple command-line blind auction system where participants can place bids without seeing other bidders' offers.

## Overview

The `blind_auction.py` program creates a competitive bidding environment where:
- Multiple users can enter their names and bid amounts
- Each bid is kept secret from other participants
- The console is cleared between entries to maintain privacy
- At the end, the highest bidder is declared the winner

## Features

- **Privacy Protection**: Bids are hidden from other participants through console clearing
- **Simple Interface**: Command-line prompts guide users through the bidding process
- **Winner Determination**: Automatically finds and announces the highest bid
- **Multiple Participants**: Supports unlimited number of bidders

## How It Works

1. The program prompts for a bidder's name
2. Asks for their bid amount
3. Clears the screen to hide the bid from the next participant
4. Asks if there are more bidders
5. Repeats until no more bidders
6. Displays the winner with their winning bid amount

## Technical Details

- Written in Python using only standard library functions
- Stores bids in a dictionary structure (bidder_name: bid_amount)
- Uses simple linear search to find the maximum bid
- Cross-platform console clearing for privacy

## Usage

```bash
python blind_auction.py
```

Follow the on-screen prompts to enter bids and complete the auction.

## Future Enhancements

- Input validation for bid amounts
- Tie-breaking mechanisms
- Persistent data storage
- GUI interface
- Network support for remote bidding
