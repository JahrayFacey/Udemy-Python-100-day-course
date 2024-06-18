#Password Generator Project- Jahray Facey 
# This is a program that will generate a random password based on user-selected criteria.
import random
#I created 3 lists of characters, numbers and symbols to generate a password that can be strong, medium or weak.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#The user inputs the criteria for the password.
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#An empty list is created tht will be used to store the password. All 3 lists are iterated through to create a sequence of characters that are then shuffled.
password = []
for char in range(1, nr_letters + 1):
 password.append(random.choice(letters))
for symb in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))
for numb in range(1, nr_numbers + 1):
  password.append(random.choice(numbers))
random.shuffle(password)
print("".join(password))
