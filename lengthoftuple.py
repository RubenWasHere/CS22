"""Length of a tuple
We can find the length of the tuple using the len() function
This will return the number of items in the tuple."""

tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
#length of a tuple
print(len(tuple1))

"""Iterating a tuple
We can itterate a tuple using a for loop let us see this with an example"""

#Create a tuple
sample_tuple = tuple((1,2,3,"Hello", [4,8,16]))
#iterate a tuple
for item in sample_tuple:
    print(item)