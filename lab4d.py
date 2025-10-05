#!/usr/bin/env python3
# Strings 1

#AuthorID: 128939238


str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str):
    return str[0:5]
    #returns the first five characters of the sring

def last_seven(str):
    return str[-7:]
    #returns the last seven characters of the string

def middle_number(num):
    number = str(num)
    return number[1:3]
    # returns the second and third number of the number provided as a string 

def first_three_last_three(str1, str2):
    first_three = str1[0:3]
    last_three = str2[-3:]
    return first_three + last_three
    # returns the first three string of arg1 and last three strings of arg2 combined


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))