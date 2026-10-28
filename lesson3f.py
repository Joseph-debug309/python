#Create a python program that determines  whether number entered is odd or even

Number = int(input("enter number here."))
if Number % 2 == 0:
    print("even")
else:
    print("odd")

#Create a python program that determines whether a person can donate blood depending on age and weight. if the age is above 18 and weight above 50kg else not possible.
age = int(input("Enter your age here"))
weight = float(input("Enter your weight here"))

if age > 18 and weight >= 50:
    print("Can donate")
else:
    print("Not possible")