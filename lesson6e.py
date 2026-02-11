#On the try and except block: You run some codes/statements and if it id succesful the try block will get executed other the except block will be executed when there is an anticipated error

try:
    number = 100
    answer = number / 0
    print(answer)
except Exception as e:
    print("There is an error", e)