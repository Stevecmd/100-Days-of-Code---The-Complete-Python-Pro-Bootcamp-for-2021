# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Method 1
#def greet(name):
#    print(f"Hi {name}" + "\n")
#    print(f"Hey {name}" + "\n")
#    print(f"Hello {name}" + "\n")

#greet("Solomon")

#Method 2
# def greet():
#   print ("Hi")
#   print ("Habari")
#   print ("Jambo")
# greet()
# 
# name=input("\nWhats your name please? ")
# def greet_with_name():
#   print (f"\nHi {name}!")
#   print (f"Habari yako {name}?")
#   print (f"Jambo {name}!")
# greet_with_name()

#Greeting with name and location
name=input("\nWhats your name please? ")
location = input("\nWhere are you from? ")
def greet_with_name():
  print (f"\nHi {name}! You are from {location}")

  print (f"Habari yako {name}?")
  print (f"Jambo {name}!")
greet_with_name()