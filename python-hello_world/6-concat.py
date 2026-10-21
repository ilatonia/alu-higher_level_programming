#!/usr/bin/python3
str1 = __import__("__main__").__dict__.get("str1", "Welcome to ")
str2 = __import__("__main__").__dict__.get("str2", "Holberton School!")
str1 = str1 + str2
print(str1)
