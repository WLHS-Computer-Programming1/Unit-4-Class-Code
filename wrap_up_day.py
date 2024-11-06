"""
Name: Mr.Smith
Date: 11/4/2024
Description: Nested Loop Practice Problems
"""

# Problem 1
# Make a 10x10 multiplication table
# 1 2 3 4  5  6  7  8  9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 ...........
# etc etc
for row in range(1,11):
    for column in range(1,11):
        print(f"{str(row*column):<4}",end = "") # this makes each product take up 3 characters

    print()
#    OR

#   1 2 3 4 ...
# 1 1 2 3 4 ...
# 2 2 4 6 8 ...
# . . . . . ...
# . . . . . ...














# Problem 2
# Ask a user for 2 numbers and make a multiplication table of that size

# Problem 3
# modify the code to print the first 100 digits of pi
with open("million_digits_pi.txt","r") as f:
    count = 0
    digits = ["0123456789"]
    print(f.read(6))



