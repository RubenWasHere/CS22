#Program asks for users name, favourite colour and two favourite numbers
#Program outpits a greeting and does some Maths...
#Created: 19/2/2021
#Author: Ruben Bharot

'''Does not check that number inputs are intergers, ie: if users don't enter an integer, program crasher'''

#Ask user for their name
name = input("What is your name? ")

#Ask user for their favourite color
fav_colour = input("What is your favourite color? ")

#Ask user for their favourite numbers
num_one = int(input("What is your favourite number? "))
num_two = int(input("What is your second favourite number? "))

#Do math!
plus = num_one + num_two
minus = num_one - num_two
times = num_one * num_two

#Output Greeting and results
print("Hello", name)
print(fav_colour, "is my favourite color too! Let's do some basic maths")

print(num_one, "+", num_two, "=", plus)
print(num_one, "-", num_two, "=", plus)
print(num_one, "*", num_two, "=", plus)