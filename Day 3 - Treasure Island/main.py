print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

road = input('You are at a cross road. Where do you go? Type "left" or "right".\n')

if road == "left":
	print("\nYou come to a lake.")
	lake = input('There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')

	if lake == "wait":
		print("\nYou arrive at the island unharmed.")
		door = input('There is a house with 3 doors: one red, one yellow, and one blue. Which colour do you choose?\n')

		if door == "yellow":
			print("\nYou found the treasure! (ɔ◔‿◔)ɔ ♥")
		elif door == "red":
			print("\nYou've enter a room with blazing fire and get burned. Game over!")
		elif door == "blue":
			print("\nYou enter a room of beasts and get eaten. Game over!")
		else:
			print("\nBetter luck next time...")

	else:
		print("\nYou've been attacked by piranhas. Game over!")
	
else:
	print("\nYou fall into a hole. Game over!")
