#python lists
#This is a collection of items that are ordered in a certain way. a list is introduced by the use of the square brackets [].
#the items of a list are stored inside of indices. Note: In programming we start programming from index zero(0)
#A list is mutable i.e the contents can be changed.

cars = ["BMW M5" , "MercedezBenz GLS 63" , "Toyota Hiace" , "Toyota Prado" , "Bentley Mullsane" , "McLaren F1" , "Range Rover Evoque"]
print(cars)
print(type(cars))

print(cars[2])

print("The car on index four is: ",cars[4])

#list slicing
#This is creating a list from a given bigger list
#This is a sliced list from index 4 forward
print(cars[4:])
#this is a sliced to index three 
print(cars[:4])
#slice index 3 - 5
print(cars[2:5])

#List - Mutability
#We use the function append to add an item at the end of a list
cars.append("Mercedez SLR McLaren")
print(cars)

cars.append("Subaru Forester")
print(cars)


#We use a pop icon to remove an item at the end of the list
cars.pop()
print(cars)

#We can use an index to add items to the list
cars[2] = "Pajero"
print(cars)

#We can use the sort function to sort this in alphabetical order
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)
del cars[4]
print(cars)
cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)