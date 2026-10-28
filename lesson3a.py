#Boolean - This is a data type that evaluates whether true/false

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

#Comparison operators - are used to compare two or more statements and they ussually return a boolean answer

number1 = 2
number2 = 5

print("is number1 greater than number2? ", number1 > number2)
print("is number1 less than number2? ", number1 < number2)
print("is number1 greater than or equal to number2? ", number1 >= number2)
print("is number1 less than or equal to number2? ", number1 <= number2)
print("is number1 equal to number2? ", number1 == number2)
print("is number1 not equal to number2? ", number1 != number2)

#logical operators:
#AND
#retuns true if and only if the condition/statements evaluates to true
print((3 > 1) and (7>6) )

#OR
#evaluates to true if one of the statementd is true
print((3 > 1) or (7 < 6) or (10<7))

#NOT
#Used to negaate a statement/condition
print(not(90 > 70))