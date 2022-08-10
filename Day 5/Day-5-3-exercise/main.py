#Write your code below this row 👇
# Method 1
# initialize the var
total = 0
# in range(a, b, c), a = start, b = end, c = step
for number in range(2, 101, 2):
    # total=total+number
    total += number
    # note += is different from =+
print(total)

# Method 2
# total=0
# for number in range(1, 101):
#   if number % 2 == 0:
#     total += number
# print(total)
