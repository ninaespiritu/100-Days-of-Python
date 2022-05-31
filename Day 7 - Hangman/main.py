import random
import hangman_art
import hangman_words

print(f"{hangman_art.logo}\n")

# Choosing a word
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives = 6

# Creating blanks
display = []

for letter in range(word_length):
  display += "_"

# Test =================================
print(chosen_word)

# Guessing letters & replacing blanks
while not game_over: 
  guess = input("Guess a letter: ").lower()
  
  # Checking if letter has already been guessed
  if guess in display:
    print(f'You have already guessed the letter "{guess}".')
    
  # Checking guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
      
    if letter == guess:
      display[position] = guess
    
  # Checking if user is wrong
  if guess not in chosen_word:
    lives -= 1
    print(f'The letter "{guess}" is not in the word. You have {lives} lives left.')

    # Losing
    if lives == 0:
      game_over = True
      print(f"\nYou lose. The word is: {chosen_word}")
      
  # Checking if user has guessed all letters
  if "_" not in display:
    game_over = True
    print("\nYou win! (ɔ◔‿◔)ɔ ♥")

  # Printing hangman and blanks
  print(f"\n{' '.join(display)}")
  print(hangman_art.stages[lives])