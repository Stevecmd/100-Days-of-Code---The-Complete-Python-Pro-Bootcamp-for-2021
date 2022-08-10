# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)  #prints all the names
print(len(names))  #prints the number of names

import random

payee = random.randint(
    0, (len(names) -
        1))  #Gives a random number, minus one because the count starts at 0
print(payee)  #prints the random number
print("Yay, ", names[random.randint(
    0, len(names)-1)] + " is catering for the meal today.")  #Gets a random number and prints the name attached to it
