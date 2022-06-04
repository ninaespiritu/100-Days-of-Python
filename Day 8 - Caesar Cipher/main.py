alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar cipher function
def caesar_cipher(text_message, shift_number, cipher_direction):
  caesar_text = ""
  
  if cipher_direction == "decode":
    shift_number *= -1
    
  for char in text_message:
    if char in alphabet:
      index = alphabet.index(char)
      new_index = index + shift_number
      caesar_text += alphabet[new_index]
    else:
      caesar_text += str(char)
    
  print(f"\nThe {direction}d text is ---> {caesar_text}")

# ASCII Art
import art
print(art.logo)

# Programme repeatability
end_caesar_cipher = False

while not end_caesar_cipher:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  
  caesar_cipher(text_message=text, shift_number=shift, cipher_direction=direction)

  restart = input("\nWould you like to go again? Type 'yes' or 'no':\n")
  if restart == "no":
    end_caesar_cipher = True
    print("\nGoodbye!")