#Create 2 strings S1 + S2 and create a third string by appending in the middle

s1 = "Auckland"

s2 = "City"

print (s1[:4] + s2 + s1[4:])

donut_price = 5

num_donuts = int(input("How many gourmet donuts would you like? "))

print("But wait! It's saturday so you get $1 off your total order for each donut purchased!")

order_total = num_donuts * (donut_price - num_donuts)

print("That will cost: ${}".format(order_total))