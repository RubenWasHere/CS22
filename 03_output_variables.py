# Display output - Three method Demonstrator
# Created 24/2/2021
# Author: Ruben Bharot

''' Asks for a seris of inputs and then displays them using three different methods'''

# Get inputs

name = input("What is your name? ")
fav_colour = input("What is your favourite colour? ")

num_one = int(input("Choose a number: "))
num_two = int(input("Choose another number: "))

#Add the numbers

plus = num_one + num_two

# Combine using string concatenation '+' method
print("Hello " + name + ". Your favourite colour is " + fav_colour)

# Combine using .format method
print("Hello {}. Your favourite colour is {}".format(name,fav_colour))

# Combine using commas method 
print("Hello", name, ". Your favourite colour is", fav_colour)

print(str(num_one) + " + " + str(num_two) + " = " + str(plus))

