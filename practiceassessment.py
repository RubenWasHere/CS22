"""This program is to ensure that children at Sunshine Holiday Camp are given the option to choose a vegetable for their evening meal"""

#Create name procedure
def campname():
    print("*****************************")
    print("*** Sunshine Holiday Camp ***")
    print("*****************************")

#Set allowed to go to yes
allowed = "yes"

#print the name of the camp at the beginning
campname()

#Ask for name and age of camper, Make name and age required, make name have letters only and age have numbers only
name = input("What is your name? ")

while any(char.isdigit() for char in name):
     print("Please enter only letters for your name.")
     name = input("What is your name? ")
     while not any(char.isalpha() for char in name):
        print("Please enter your name")
        name = input("What is your name? ")

while not any(char.isalpha() for char in name):
        print("Please enter your name")
        name = input("What is your name? ")
        while any(char.isdigit() for char in name):
            print("Please enter only letters for your name.")
            name = input("What is your name? ")

age = input("What is your age? ")

while any(char.isalpha() for char in age):
    print("Please do not include letters in your age")
    age = input("What is your age? ")
    while not any(char.isdigit() for char in age):
        print("Please enter your age")
        age = input("What is your age? ")

while not any(char.isdigit() for char in age):
    print("Please enter your age")
    age = input("What is your age? ")
    while any(char.isalpha() for char in age):
        print("Please do not include letters in your age")
        age = input("What is your age? ")

#Convert string to int
age= int(age)

#If age < 7 or > 12 ineligible
if age < 7:
    print ("You are too young to be eligible for this camp.") 
    allowed = "no"
    campname()
if age > 12: 
    print ("Your are too old to be eligible for this camp.") 
    allowed = "no"
    campname()

#Create and print list for vegtable choices
def list():
    veglist = ["carrots", "cucumber", "radish", "tomato", "mixed peas and corn", "butter parsnip"]
    count = 0
    while count < len(veglist):
        print (veglist[count])
        count = count + 1
        print()

if age <= 10 and allowed == "yes": 
    list()
    vegtable = input("What vegtable would you like to have for dinner? ")
    
    while vegtable.lower() not in {"carrots", "cucumber", "radish", "tomato", "mixed peas and corn", "butter parsnip"}:
            print()
            list()
            print("Ensure your spelling is correct!")
            vegtable = input("What vegtable would you like to have for dinner? ")

if age <= 10 and allowed == "yes": 
    if vegtable.lower() in {"carrots", "cucumber", "radish", "tomato", "mixed peas and corn", "butter parsnip"}:
        print()
        print (name.capitalize(), "is", age, "years old", "and has selected the vegtable", vegtable.lower())
        campname()

if age > 10 and allowed == "yes":
    print (name, "is", age, "years old")
    campname()

