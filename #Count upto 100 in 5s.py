#Ruben Bharot
#17/03/21
#User input counter

#Ask user what number the program should count up to
upto = int(input("What number should I count up to? "))

#Ask user what number the program should count up in
upin = int(input("What number should I count up in? "))

#count upto
count = 0 
while count <= upto:
    print(count)
    count = count + upin