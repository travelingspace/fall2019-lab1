#Part 4: camelCase

#Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, 
# and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser".
#Optional: can you do this with a list comprehension?

#Optional extra question: print a warning message if the input will not produce a valid variable name. You don't need to be exhaustive in checking, 
# but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".  

sentenceInp = input("Please provide a complete sentence to be camelCase-isized:")

wordList = sentenceInp.split(" ")
outputStr = ""

for i in range(0, len(wordList)):
    newWord = wordList[i].lower()
    if i != 0:
        newWord = newWord.capitalize()
           
    outputStr = outputStr + newWord

print(outputStr)


