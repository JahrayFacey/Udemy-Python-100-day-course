# This is my personal project of a Ceaser cipher
# I created a list with the the whole alphabet in order twice. The reason for this is to accomodate for the shift amount

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# I combined the encrypt() and decrypt() functions into a single function called caesar(). The inputted message is iterated and shifted by the shift amount. The shifted message is then printed.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
# If the user enters a number/symbol/space, instead of shifting the letter, it will just be concated to the end_text
      else:
        end_text += letter
  print(f"The encoded text is {end_text}")
    
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#if direction == "encode":
#  encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
#  decrypt(cipher_text=text, shift_amount=shift)

# The loop will continue until the user enters "no"
resume = True
while resume == True:
# The user is asked to enter a message, the shift amount, and whether they want to encode or decode it
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
# The shift amount is adjusted to fit the list
  shift = shift % 26
# The caesar() function is called
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
# The user is asked if they want to continue
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    resume = False
    print("Goodbye")
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
  result = input("Do you want to continue? Type 'yes' or 'no'.\n")
  if result == "no":
    resume = False
#Original functions for encrypt and decryption included