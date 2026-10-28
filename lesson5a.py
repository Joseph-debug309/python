#python Functions
#These are blocks of code/statements that pperform a given task/ function. They can be used in the prog to perform diffrent tasks.
#Python functions are defined using the def key word
#We have two types of functions:
#1. In-build - come preinstalled with the interpreter i.e print(), pop(), range(), append()
#2. User defined - Are created by a proggrammewe to solve a given task.
#To define a function you need to give it a name followed by parenthesis.
# For the function, it is usually indented and to invoke a function we use the function name.

def greetings():
    print("Hello, how are you?")

#Below we xall the function by its name
greetings()

print("___________________________________")
#Additional function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("the sum of the numbers is", sum)

addition()

print("___________________________________")
#Create a function that is able to multiply three values

def multi():
    num1 = 2
    num2 = 12
    num3 = 15
    product = num1 * num2 * num3
    print("The product of the numbers is", product)

multi()

print("___________________________________")
#Below is a division function

def divide():
    number1 = int(input("Enter your first number here:   "))
    number2 = int(input("Enter your second number here:  "))
    Quotient = number1 / number2
    print("the answer is: " , Quotient)
    print("--------")

for function in range(3):
    print("Enter new data")
    divide()
    