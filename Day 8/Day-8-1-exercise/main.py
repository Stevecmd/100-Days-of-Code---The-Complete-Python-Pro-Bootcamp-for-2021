#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width)/cover)
  # round_up_cans = math.ceil(number_of_cans)
  # print(f"You'll need {round_up_cans} cans of paint.")
  print(f"You'll need {number_of_cans} cans of paint.")


print("You will need {number_of_cans} of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5 #1 can of paint can cover 5 square meters of wall
paint_calc(height=test_h, width=test_w, cover=coverage)


