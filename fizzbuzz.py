#!/usr/bin/python3
import time
#Take the user input
choice = int(input("Please enter the number of your choice"))
#function definition
def function(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")

        elif num % 5 == 0:
            print("buzz")
        else:
            print("num")
    print("Your program will run shortly")

    time.sleep(5)
    function(choice)
