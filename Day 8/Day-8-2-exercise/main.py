#Write your code below this line 👇
# import math
def prime_checker(number):
  
    # Corner case
    if number <= 1:
        print ("False")
    
    # Check from 2 to n-1
    for num in range(1, number):
        if number ==2:
          print ("True")
          break;
        if number % num == 0:
           print ("False");
        break;
    else:
      print ("True");
 
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



