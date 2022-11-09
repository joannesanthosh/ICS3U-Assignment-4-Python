#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program identifies which quadrant the coordinate is in

import math


def main():
    # this function identifies if a number is even or odd

    # input
    user_input_as_string = input("Enter any integer(positive or negative): ")
    print("")

    # process
    try:
        user_input = int(user_input_as_string)
        if user_input % 2 == 0:
            print("{0} is an even number.".format(user_input))
        else:
            print("{0} is an odd number.".format(user_input))
    except ValueError:
        print("{0} is not an integer.".format(user_input_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
