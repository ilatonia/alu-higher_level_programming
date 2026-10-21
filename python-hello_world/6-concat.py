#!/usr/bin/python3
str1 = globals().get('str1', "Welcome to ")
str2 = globals().get('str2', "Holberton School!")
str1 = str1 + str2
print(str1)
