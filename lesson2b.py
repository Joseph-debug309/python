#Tuple
#This  is an immutable type of a list
#To introduce we use parenthesis

Counties = ("Nairobi" , "Nakuru" , "Kiambu" , "Eldoret" , "Kisii")
print(Counties)

#slicing of tuples
print(Counties[3:])

#Accesing items using Indexes
print(Counties [5])

#Note - will produce an error
Counties.append("Machakos")
print(Counties)