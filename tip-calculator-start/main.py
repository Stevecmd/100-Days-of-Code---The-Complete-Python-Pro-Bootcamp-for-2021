#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇
total=int(input("What was the total bill? "))
people=int(input("How many people shared the meal? "))
division = (total/people) * 1.12
tip = str(total * 0.12)
answer = str(round(division, 2))
print ("Each person will have to pay " + answer)
print ("The tip total is " + tip)

