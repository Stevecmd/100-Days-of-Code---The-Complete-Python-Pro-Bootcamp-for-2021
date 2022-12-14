# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input(str("What is your name? \n"))
name2 = input(str("What is their name? \n"))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

# Python3 code to demonstrate
# occurrence frequency using
# re + findall()
import re
# using re + findall() to get count
# counting e, we combine the names so as to count only once
names = name1.lower() + name2.lower()
# we use lower case because count is case sensitive
true = len(re.findall("t", names)) + (len(re.findall("r", names))) + (len(
    re.findall("u", names))) + (len(re.findall("e", names)))
love = len(re.findall("l", names)) + len(re.findall("o", names)) + len(
    re.findall("v", names)) + len(re.findall("e", names))
count = int(f"{true}" + f"{love}")
# printing result
if (count < 10) or (count > 90):
    print(f"Your score is {count}, you go together like coke and mentos.")
elif (count >= 40) and (count <= 50):
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")

#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('main.py', 'r') as original:
        f2 = original.readlines()[0:60]
        for x in f2:
            file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os


class MyTest(unittest.TestCase):
    def run_test(self, given_answer, expected_print):
        with patch('builtins.input', side_effect=given_answer), patch(
                'sys.stdout', new=StringIO()) as fake_out:
            testing_copy.test_func()
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_1(self):
        self.run_test(
            given_answer=['David Beckham', 'Victoria Beckham'],
            expected_print=
            'Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n'
        )

    def test_2(self):
        self.run_test(
            given_answer=['Han Solo', 'Princess Leia Organa'],
            expected_print=
            'Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n'
        )

    def test_3(self):
        self.run_test(
            given_answer=['Pierre Curie', 'Marie Curie'],
            expected_print=
            'Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n'
        )

    def test_4(self):
        self.run_test(given_answer=['Mark Antony', 'Cleopatra'],
                      expected_print=
                      'Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print(
    'Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n'
)
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py')
