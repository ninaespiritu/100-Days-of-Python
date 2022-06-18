import random
from os import system as s
def clear():
  s("clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
  return random.choices(cards, k = 2)

cards_player = deal_cards()
cards_computer = deal_cards()

def calculate_score(x):
  return sum(x)

# Blackjack
def game():
  should_continue = True

  while should_continue:
    score_player = calculate_score(cards_player)
    score_computer = calculate_score(cards_computer)
    print(f"    Your cards: {cards_player}, current score: {score_player}")
    print(f"    Computer's cards: [{cards_computer[0]}, ?]")
    
    get_new_card = input("\nType 'y' to get another card, type 'n' to pass: ")
    
    if get_new_card == "y":
      deal_card = random.choice(cards)
      cards_player.append(deal_card)
      score_player = calculate_score(cards_player)
      
    else:
      while score_computer < 17:
        deal_card = random.choice(cards)
        cards_computer.append(deal_card)

      print(f"\n    Your final hand: {cards_player}, final score: {score_player}")
      print(f"    Computer's final hand: {cards_player}, final score: {score_player}")
      
      if score_computer > 21:
        print("YOU WIN!")
      else:
        if score_player == score_computer:
          print("IT'S A DRAW.")
        elif score_player < score_computer:
          print("YOU LOSE.")
        elif score_player > score_computer:
          print("YOU WIN!")

game()