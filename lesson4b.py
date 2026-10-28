# Loops
# sometimes we may need to do a piece of work a multiple no of times. in such cases we use a loop.
# a looop is a control structure that allows you to execute the code till the condition is met.
# there are two types of loops in python: The for loop and while  loop

# Below is the syntax of a for loop in python
"""
for variable in range(n):
    #block of statements to be executed
"""

for greeting in range(5):
    print("Hello Moses" , greeting)

print("---------------------------------------")

for number in range(10, 20):
    print(number)

print("_____________________________")

for number in range(50, 71, 2):
    print(number)

print("____________________________________")

#Create a pyhton program that allows one to print odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print("____________________________________")

#Create a program that prints the multiples of three starting from 201 to 150
for number in range(201, 150, -3):
    print(number)

print("____________________________________")
#Create a python prog that prints leap years btwn 2000 and 2024
for year in range(2000, 2024, 4):
 print(year)