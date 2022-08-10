import random

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

#Write your code below this line 👇
images = [rock, paper, scissors]
choice = int(
    input("Rock, paper or scissors? Please type 0, 1 or 2 respectively."))
if choice >= 3 or choice < 0:
    print("Please provide valid input")
else:
    print(images[choice])
    signs = ["rock", "paper", "scissors"]

    # random selection by computer
    rand_sign = int(random.random() * len(signs))
    random_num = signs[rand_sign]
    print(images[rand_sign])
    print(f"Computer chose {random_num}\n")

    # game logic
    if choice == rand_sign:
        print("draw")
    elif rand_sign == 0 and choice != signs[0]:
        print("Computer wins 1")

    elif rand_sign == 1 and choice != signs[2]:
        print("Computer wins 2")

    elif rand_sign == 2 and choice != signs[1]:
        print("Computer wins 3") 
    else:
      print("You won.")