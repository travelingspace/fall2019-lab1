#Part 2: List of classes

#Write a program that asks for the names of all of the classes you are taking this semester
classNames = input("List out your class names, separated by commas: ")
classList = classNames.split(",")

for i in range(0, len(classList)):
    print(classList[i],"\n")
#Save these class names in a list.
#Print all the items in the list, one per line.