#Part 3: Guess the number

#Write a 'guess the number' game. The computer should 'think' of a random number within a certain range, and challenge the user to guess the number. 
# Provide feedback and hints for the user; such as "too high" or "too low".  Don't forget to comment your code.

import random

number = random.randint(1,10)
guess = input("Guess a number between 1 and 10. You can keep guessing if you get it wrong:\n")

while int(guess) != number:
    
    if int(guess) < number:
        guess = input("Too low. Keep trying!:\n")
    else:
        guess = input("Too high. Keep trying\n")

else:
    print("Congrats! You guessed right")
        

    