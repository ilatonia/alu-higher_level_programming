#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        n = -n
    last = n % 10
    print("{}".format(last), end="")
    return last
