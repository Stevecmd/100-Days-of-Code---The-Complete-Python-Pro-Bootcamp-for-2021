#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# random_list = [random.randint(0, 9) for i in range(nr_numbers)]
# print(random_list)

password = ""
# initialize password

import string

length_of_string = nr_letters
letters = string.ascii_letters
random_string = ""
random_numbers = ""
for number in range(length_of_string):
    random_string += random.choice(letters)
# print(random_string)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
# print(password)

# random_list = [random.randint(0, 9) for i in range(nr_numbers)]
# print(random_list)

for number in range(nr_numbers):
    random_numbers += random.choice(numbers)
# print (random_numbers)

password = (random_string) + (password) + (random_numbers)
# concatenating the newly generated password
password_list = list(password)
# for shuffle to work, the pasword must be in a list
random.shuffle(password_list)
# putting the shuffled characters back together to form the new password
result = ''.join(password_list)

# print (password_list)
# printing the password_list out of curiosity

print("\nYour new password is: ", (result))
# final password_list
