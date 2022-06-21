import random
from art import logo
from os import system as s
def clear():
  s('clear')

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# FUNCTION: Calculate score of list of cards
def calculate_score(cards):
  # If blackjack (ace + 10), set blackjack value to 0
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # If ace and score over 21, replace 11 with 1
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# FUNCTION: Compare scores
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "\nIt's a draw..."
  elif user_score == 0:
    return "\nYou have a Blackjack. You win!"
  elif computer_score == 0:
    return "\nYour opponent has Blackjack. You lose."
  elif user_score > 21:
    return "\nYou went over. You lose."
  elif computer_score > 21:
    return "\nYour opponent went over. You win!"
  elif user_score > computer_score:
    return "\nYou win!"
  else:
    return "\nYou lose."

# FUNCTION: BLACKJACK GAME
def play_game():
  
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  # Deal the user and computer 2 cards each
  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  # WHILE LOOP: User plays
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    YOUR CARDS: {user_cards}, CURRENT SCORE: {user_score}")
    print(f"    COMPUTER'S CARDS: [{computer_cards[0]}, ?]\n")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_deal = input("Type 'y' to get another card, type 'n' to pass: ") 
      if user_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
        
  # WHILE LOOP: Once user is done, computer plays
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"    YOUR FINAL CARDS: {user_cards}, FINAL SCORE: {user_score}")
  print(f"    COMPUTER'S FINAL CARDS: {computer_cards}, FINAL SCORE: {computer_score}")
  print(compare(user_score, computer_score))

# Restart game
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()