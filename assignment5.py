#Non-paramter function that uses arithmetic functions to calculate the area of a triangle

def area():
    l = int(input("Enter length here: "))
    w = int(input("Enter width here: "))
    A = l * w
    print("The area is: ", A)

area()
#Parametric function 

def num(y, z):
    num1 = y
    num2 = z
    sum = num1 + num2
    diffrence = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    print(sum)
    print(diffrence)
    print(product)
    print(quotient)

num(3 ,4)

#Control statement

n = int(input("Enter a number here: "))

if n > 0:
    print(n, "is positive")
elif n == 0:
    print(n, "is zero")
elif n < 0:
    print(n, "is negative")
else:
    print("invalid input") 

#loop with arithmetic
n = int(input("ENTER NUMBER HERE"))
sum = 0
total_sum = 0

for i in range(1, n + 1):
    total_sum+=i
    print(total_sum)


#While loop that prints squares from 1 to n
n = int(input("enter here"))
i = 1
while i <= n:
    square = i**2
    print(square)
    i += 1