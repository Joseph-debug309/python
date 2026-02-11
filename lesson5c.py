# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.
def simpleintrest(p, r, t):
    SI = p * r * t / 100
    print(SI)

simpleintrest(45000, 7, 8)

#loop for two others
intrests = [
    (40000, 4, 5),
    (56000, 3, 8)
]

for p, r, t in intrests:
    simpleintrest(p, r, t)