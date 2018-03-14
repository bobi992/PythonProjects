__author__ = 'X'

import random

number = random.randint(50, 60)
tries = 1
win = False # setting a win flag to false


name = input("Hello, What is your username?")

print("Hello", name + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print("Shame on you")

if question == "y":
    print("Hmmmm... I'm thinking of a number between 50 & 60")
while not win:
    guess = int(input("Have a guess: "))
    tries = tries + 1
    if guess == number:
        win = True
    elif guess < number:
        print("Guess Higher!")
    elif guess > number:
        print("Guess Lower!")
if win:
    print("Congrats, you guessed correctly. The number was indeed {}".format(number))
    print("it had taken you {} tries".format(tries))