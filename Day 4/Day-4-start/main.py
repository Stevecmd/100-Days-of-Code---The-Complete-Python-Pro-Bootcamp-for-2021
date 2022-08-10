import random

random_side = random.randint(0, 1)  #get a random number between 0 and 1  
print (random_side) #prints the random number 
if random_side == 1:
    print("Heads")
else:
    print("Tails")


