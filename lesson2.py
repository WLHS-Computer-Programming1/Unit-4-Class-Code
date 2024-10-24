'''
Name:
Date: 10/24/24
Description: For loops
'''

# For loop style 1 - for i in range(stop)
# this prints 0, 1, 2, 3, 4 each on their own line
# the number in range(stop) is how many nums are printed
# starting at 0 and ending at num-1

# common use: doing a known number of things
for i in range(5):
    print(i)

# nums on same line
for i in range(5):
    print(i,end=" ")
print()
for i in range(5):
    print(i,end=", ")

# For loop style 2 - for i in range(start, stop)
# this prints start, start+1, ...., stop-1
# loop runs stop-start number of times
for num in range(2,6):
    print("*"*num)

for num in range(2,6):
    print(num,end= " ")
###################################################
print("")
print(f"---------")
print(f"x  | x^2")
for num_to_square in range(1,6):
    print(f"{num_to_square}  | {num_to_square**2}")
print(f"---------")

# For loop style 3 - for i in range(start, stop, step)
# this prints start, start+1, ...., stop-1 but counts by step
# loop runs ceiling((stop-start)/step) times
# ceiling means round up to nearest int
for number in range(10,40,4): # want: 10 to 40 counting by 4s
    print(number, end = " ")

# want: start at 12, count by 7s up to but not past 93
print()
for number in range(12,93,7):
    print(number, end = " ")
print()
for number in range(12, 94, 7):
    print(number, end=" ")
print()

##################################
# print the sum of the numbers 1 through n

user_num = int(input("Give me a number: "))
sum = 0 #initialize our sum to 0
for num in range(1,user_num+1):
    sum = sum + num

print(f"The sum is {sum} ")

###################################

# 1) ask the user to enter 5 numbers (hint: use a loop)
# 2) find the average of those numbers (hint: use a loop)
# 3) print "the average of your numbers is -----"

average = 0
num_1 = int(input("Give me a number: "))
num_2 = int(input("Give me a number: "))
num_3 = int(input("Give me a number: "))
num_4 = int(input("Give me a number: "))
num_5 = int(input("Give me a number: "))
average = num_1 + num_2 + num_3 + num_4 + num_5
average = average/5
print(average)

user_sum = 0
num_values = 5
for i in range(num_values):
    user_num = int(input("Enter a number: "))
    user_sum = user_sum + user_num # updates user_sum with user_num value

average = user_sum/num_values

print(f"The average of your numbers is {average}")