print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print(
    "Welcome to Treasure Island! Your mission is to find the treasure. Where do you want to go first."
)
prompt1 = input("Left or right? \n").lower()
if prompt1 == "left":
    prompt2 = input(
        "You\'ve come to the edge of the reef. If you Swim you might escape if you wait, you may wait forever. Swim or wait? \n"
    ).lower()
    if prompt2 == "wait":
        prompt3 = input(
            "There are three doors ahead, pick one: Red, Blue or Yellow \n"
        ).lower()
    else:
        print("You got attacked by killer trout and died. Game Over.")
    if prompt3 == "red":
        print("You got burned by by an infernal fire. Game Over.")
    elif prompt3 == "blue":
        print("You got eaten by beasts from the deep. Game Over")
    elif prompt3 == "yellow":
        print("You win. Good choices brought you success, nice!")
    else:
        print("Game Over. Perhaps try again")
else:
    print(
        f'You fell into a gaping hole and broke most of your bones.\nGame Over. \nPerhaps try again'
    )
