# Blind Auction project
def blind_auction(bidder):
  # TODO-1: Ask the user for input
  name = input("What is your name: ")
  price = int(input("What is your bid: $"))

  # TODO-2: Save data into dictionary {name: price}
  bidder[name] = price

  # TODO-3: Whether if new bids need to be added
  another_bid = input("Are there any other bidder? Type 'Yes' OR 'No': \n").lower()
  return another_bid


bidder = {}
auction_running = True
current_bid = 0

while auction_running:
  new_bidder = blind_auction(bidder)
  if new_bidder == 'no':
    auction_running = False

print("All bids: ", bidder)

# TODO-4: Compare bids in dictionary
#After collecting all bids
if bidder:
    highest_bidder = max(bidder, key=bidder.get)
    print(f"The winner is {highest_bidder} with a bid of ${bidder[highest_bidder]}")
else:
    print("No bids were placed.")








