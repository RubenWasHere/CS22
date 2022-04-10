''' Program Aliens Have Landed'''

import random 
names = []
ages = []

print("Please emter the name of the first earthling, use XXX to end ")
name_in = input()

while name_in != 'XXX':
    age_in = int(input("Please enter age of earthling "))

    names.append(name_in)
    ages.append(age_in)

    print("Please enter the name of the next earthling, use XXX to end")

