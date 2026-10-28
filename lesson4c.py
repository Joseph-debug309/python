# A for loop can also be used to iterate through a tuple, list, string or even a dictionary..

name = "Joseph"
for letter in name:
    print(letter)
    if letter == "s":
        print("letter is s")
    else:
        print(letter)


print("________________________________________")
#below is a list of counties
counties = ["Nairobi" , "Mombasa" , "Nakuru" , "Eldoret" , "Kiambu"]

for county in counties:
    print(county)

print("________________________________________")

search = str(input("Enter county to search"))

found = False
for county in counties:
    if county == search:
        found = True
        break

if found:
        print(county, "is part of list")
else:
    print(county, "is not part of the list")

#for loop can be used in a dictionaty

player = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["PSG" , "Monaco" , "France" ] ,
    "Nationality" : "French"

}

for key in player:
    print(key)


for value in player:
    print(player[value])

#loop through the teams

print("________________________________")

for teams in player["teams"]:
    print(teams)

    