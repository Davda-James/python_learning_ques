#a. using different math module functions 
import math
x=23.5312
print(math.ceil(x))
print(math.floor(x))
print(round(x,3))
print(type(round(x,3)))
print(format(x,'.3f'))
print(type(format(x,'.3f')))
print("the differece of round and format is: ",float(format(x,'.3f'))-round(x,3))

#b. using in built str functions
str=input("enter a string: ")
print(str.isalpha())
print(str.isspace())
print(str.isnumeric())
print(str.isalnum())
