import random

print("Welcome to Rock Paper Scissors!\n")

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

player = int(input("What do you choose: 0 = ROCK, 1 = PAPER, 2 = SCISSORS ---> "))

if player == 0:
	print(rock)
elif player == 1:
	print(paper)
elif player == 2:
	print(scissors)

computer = random.randint(0, 2)
print("Computer chose:")

if computer == 0:
	print(rock)
elif computer == 1:
	print(paper)
elif computer == 2:
	print(scissors)

# Results
if player >= 3:
	print("You typed an invalid number. Better luck next time...")
elif player == 0 and computer == 2:
	print("\nYOU WIN! (ɔ◔‿◔)ɔ ♥")
elif player == 2 and computer == 0:
	print("\nYOU LOSE.")
elif player > computer:
	print("\nYOU WIN! (ɔ◔‿◔)ɔ ♥")
elif player < computer:
	print("YOU LOSE.")
elif player == computer:
	print("IT'S A DRAW!")
