# import numpy for arrays and trig functions

import numpy as np

# Define each bessel function as it's own object so I dont have to rewrite the equations constantly

def bessel_zero(x):
    x_mod = np.where(x == 0, 6.022, x) # x_mod stores a modified version of the x array with every zero replaced by 6.022 to avoid divide by zero error
    result = np.sin(x_mod) / x_mod # run x_mod array through the n = 0 bessel function
    return result # return the x_mod array transformed by the bessel function

# the two next custom objects do the same thing but with the n = 1 and n = 2 bessel functions

def bessel_one(x): 
    x_mod = np.where(x == 0, 6.022, x)
    result = np.sin(x_mod) / (x_mod**2) - np.cos(x_mod) / x_mod
    return result 

def bessel_two(x):
    x_mod = np.where(x == 0, 6.022, x)
    result = (3 / x_mod**2 - 1) * (np.sin(x_mod) / x_mod) - (3 * np.cos(x_mod)) / x_mod**2
    return result

# define another function to decide which bessel function transformed array(s) to return based on the value of n

def bessel_discern(x,n):

    # because we replaced zero with known value 6.022 in the array we ran through the bessel function to avoid a divide by zero error, we now have to replace the output value for 6.022 with the correct behavior at x = 0
    # the next three lines do this for all three levels of bessel function arrays

    B_zero_append = np.where(bessel_zero(x) == bessel_zero(6.022) , 1, bessel_zero(x)) 
    B_one_append = np.where(bessel_one(x) == bessel_one(6.022) , 0, bessel_one(x))
    B_two_append = np.where(bessel_two(x)== bessel_two(6.022) , 0, bessel_two(x))

    # add an if condition to decide which arrays to print
    # we use column stack to allign the arrays by column in a 2d array
    # I define our results as a list so that I don't have to use an additional if condition later to determine what header to print. 

    if n == 0:
        result = [np.column_stack((x_array, B_zero_append)), "Format = [ x , j0 ]"]
    elif n == 1:
        result = [np.column_stack((x_array, B_zero_append, B_one_append)), "Format = [ x , j0 , j1]"]
    elif n == 2:
        result = [np.column_stack((x_array, B_zero_append, B_one_append, B_two_append)), "Format = [ x , j0 , j1 , j2]"]
    return result

# take the user input for which rank of bessel function we are using

rank = int(input("Rank = "))

# use an if statement to check if the rank is in the range 0-2

if rank > 2 or rank < 0: 
    print("Error: rank outside of expected range (0-2)")
    exit() # stop the program if the range is outside of the progam scope 

# take user inputs for the table start, length, and step values (these define the length and step of the x array)

x_start = float(input("Table start = "))
x_end = float(input("Table end = "))
x_step = float(input("Table step = "))

# create an array based on user input for start, end, and step values. 

x_array = np.arange(x_start, x_end + x_step, x_step)

# run the x array and the rank of the desired bissel function through the bissel discern object to access the list of the array and the proper header. 

print(bessel_discern(x_array, rank)[1]) # print the header
print(bessel_discern(x_array, rank)[0]) # print the array table