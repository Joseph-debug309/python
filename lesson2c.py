#A dictionary is a data type that stores data in terms of key - value pair.
#it is introduced by the use of callibraces{} 
#The values strored inside of a dictionary can be of any data type
#To access the values in a dictionaty we use the keys


phonebook = {
    "Benson" : "0712365776" ,
    "Mary" : "0745637839" ,
    "stephen" : "0789243567"
    }

#Show the
print(phonebook)
print(phonebook["Benson"])

print('======================')

player = {
    "Name" : "Messi" , 
    "Age" : 40 ,
    "Teams" : ["PSG", "Barcelona", "Argentina"]
}
#Print barcelona - the second tean

print(player)
print(player["Teams"][1])