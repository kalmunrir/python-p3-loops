#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i = i-1
    print("Happy New Year!")

def square_integers(int_list):
    return [num * num for num in int_list]

def fizzbuzz():
    i = 1;
    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1
