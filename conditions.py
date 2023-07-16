#!usr/bin/pythom3

def confirm_number(num):
    
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")


if __name__ == "__main__":

    try:
        user_input = float(input("ENter a number: "))
        confirm_number(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
