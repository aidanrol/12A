#In python variables are pieces of storage in RAM which can change during runtime E.g:
string = "Hello world!"  #Data is assigned to variables using "="

#Python can also collect input with the input() function:
userInput = input("Input here: ")

#Python is also able to output to the terminal/console with the print() function:
print (userInput)

#Python is able to change the datatype of data via casting:
print(int(236.0)) #Converts a float to an integer
print(str(12)) #Converts an integer to a string
print(float(18)) #Converts an integer to a float

#String handling methods:
print(string.split()) #split each word.
print(string.upper()) #makes everything uppercase.
print(string.lower()) #makes everything lowercase.
print(string.capitalize) #capitalizes the string

#You can access individual characters in a string with:
print(string[0])

#Python have if, elif, and else:
#if the condition is met...
if "hello" == "hello":
    print("condition is met")
#else if this condition is met
elif "friday" == "friday":
    print("condition is met")
#Else works if none of the other conditions are met
else:
    print("Other conditions aren't met")

#For loops are loops that continue whilst they are in a range of something:
for i in range(0, 5):
    print(i)

#While loops continue until a condition is met
i = 0
while i != 7:
    i += 1

#Subroutines are pre written peices of code which can be reused by calling the function
#They can also take parameters
def helloWorld(name):
    print("Hello world! " + str(name))

helloWorld("Aidan")