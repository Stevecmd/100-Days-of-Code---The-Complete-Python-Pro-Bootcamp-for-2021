# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇

total_height = 0
#Above we are initializing the height count.

# my_list below can be used to show the user the heights he has entered
# we dont need to use split again since the heights are split
# at student_heights
# my_list = list(map(int, student_heights))
# print("\nThe Heights given are:", (my_list))

for height in student_heights:
    total_height = +height
print(f" The total height is {total_height}")
# print("\nThe total height is", (total_height))

student_number = 0
for student in student_heights:
    student_number += 1
print("\n", "The number of students is", (student_number))
# print("\nThe number of students is", (student_number))

average = round(total_height / student_number)
print("\n", "The average height is", (average))

# \n --prints in a new line
#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('main.py', 'r') as original:
        f2 = original.readlines()[0:40]
        for x in f2:
            file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os


class MyTest(unittest.TestCase):
    def run_test(self, given_answer, expected_print):
        with patch('builtins.input', return_value=given_answer), patch(
                'sys.stdout', new=StringIO()) as fake_out:
            testing_copy.test_func()
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_1(self):
        self.run_test(given_answer='180 124 165 173 189 169 146',
                      expected_print='164\n')

    def test_2(self):
        self.run_test(given_answer='150 142 185 120 171 184 149 199',
                      expected_print='162\n')

    def test_3(self):
        self.run_test(given_answer='24 59 68', expected_print='50\n')


print("\n\n\n.\n.\n.")
print(
    'Checking that your code prints a single number - the average height - rounded to the nearest integer for several different lists of heights.\n'
)
print('\nRunning some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py")
