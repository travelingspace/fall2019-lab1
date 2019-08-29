#Part 1: Hello, birthday month

#Write a program that asks for your name and the month you were born in.
name = input('What is your name?\n')
month = input('What month were you born?\n')

#Then, your program should print

#A greeting to you, using your name
print("Hello, ", name,". Welcome to the Matrix.")
#A message with the number of letters in your name
print("There are ",len(name)," letters in your name.")
#A 'Happy birthday month!' messageS if you were born in AugustJ
if month == "August":
    print("Happy birthday month!")