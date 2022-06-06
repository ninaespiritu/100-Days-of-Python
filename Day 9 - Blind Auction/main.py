from art import logo
from os import system as s
def clear():
  s('clear')

bids = {}
auction_done = False

# FUNCTION: Adding new people and bid prices
def new_bid():
  print(logo)
  print(f"\nWelcome to the Blind Auction. There are currently {len(bids)} bids.")
  new_name = input("\nWhat is your name? ")
  new_price = int(input("What is your bid? £"))
  bids[new_name] = new_price

# FUNCTION: Checking highest bidder
def find_auction_winner():
  highest_bidder = ""
  highest_price = 0
  
  for bidder in bids:
    current_price = bids[bidder]
    if current_price > highest_price:
      highest_price = current_price
      highest_bidder = bidder
      
  print(logo)
  print(f"\nThe winner is {highest_bidder}, with a bid of £{highest_price}. Congratulations!")

# WHILE LOOP: Blind auction programme
while not auction_done:
  new_bid()
  continue_bidding = input("\nAre there any other bidders? (Type 'yes' or 'no') ") 
  
  if continue_bidding == "no":
    auction_done = True
    clear()  # print("\x1B[2J")
    find_auction_winner() 
  elif continue_bidding == "yes":
    clear()