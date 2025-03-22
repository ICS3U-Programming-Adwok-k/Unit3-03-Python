#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 21st, 2025
# This program asks the user to guess a number
# between 0 and 9

import random


def main():
    random_variable = random.randint(0, 9)

    #
    user_number = int(input("Enter a number between 0 and 9: "))
    print("")

    if random_variable == user_number:
        print("You guessed correctly! ")

    else:
        if random_variable != user_number:
            print("You guessed wrong")
            print("The correct number is " + str(random_variable))


if __name__ == "__main__":
    main()
