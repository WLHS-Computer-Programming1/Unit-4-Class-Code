'''
Write a program that makes the user guess a particular number between
1 and 100.
Save the number to be guessed in a
variable called magic_number.

If the user guesses a number higher than the secret number, 
you should say Too high!. Similarly, you should say Too low! if they guess
a number lower than the secret number.
Once they guess the number, say Correct!
'''

import random

magic_number = random.randint(1,1000)
try_count = 0
while True:
    user_guess = int(input("Guess the magic number! "))
    if user_guess > magic_number:
        print("Too high!")
        try_count += 1
    elif user_guess < magic_number:
        print("Too low!")
        try_count += 1
    elif user_guess == magic_number:
        print("You got it!")
        break

    if try_count == 7:
        print(f"Try again! The magic number was {magic_number}")
        break



