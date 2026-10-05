# import libraries

import matplotlib.pyplot as plt # matplotlib for plot functionality
import numpy as np # numpy for arrays
from math import * # math for math

#A1

# define our function f(x) so that I don't have to type the expression a million times

def f(x): 
    result = x ** 4 - 2 * x + 1 
    return result

# define our trapezoidal approximation function 

def trapezoid(f, a, b, N): # the approximation is dependent on the function we are approximating, the interval (from a to b) and the number of trapezoids we want to use.
    h = (b - a) / N # define our step size
    s = .5 * (f(a) + f(b)) # becuse the heights of the boundary values of our approximation inteval are only counted once, instead of twice like the rest of the values, we can bring them outside of the summation.
    for n in range(1, N): # use a for loop to sum the rest of the heights
        s += f(a + n * h)
    total = h * s # multiply the total by h to get the total area under the curve
    return total

#A2

def numerical_error(expected, measured): # define a function for our numeral error to to make later parts more streamlined
    result = abs(expected - measured)
    return result

def percent_error(expected, measured): # define a function for percent error for the same reason (not neccesary but I thought it would be a usefull addition)
    result = abs((expected - measured) / measured) * 100
    return result 

# use blank print statements to create breaks in terminal output to make results easier to read
# display data with formatted strings for easy labeling

print()
print("Results for A2")
print(f"N = 10 approximation: {trapezoid(f,0,2,10): .6f}")
print(f"Numerical error: {numerical_error(4.4, trapezoid(f,0,2,10)): .6f}")
print(f"Percent error: {percent_error(4.4, trapezoid(f,0,2,10)): .3f} %")
print()

#A3
 
# literally the same thing as the last problem just change up the value of N to 1 in all of my trapezoidal approximation functions. 

print("Results for A3:")
print(f"N = 1 approximation: {trapezoid(f,0,2,1)}")
print(f"Numerical error: {numerical_error(4.4, trapezoid(f,0,2,1)): .6f}")
print(f"Percent error: {percent_error(4.4, trapezoid(f,0,2,1)): .3f} %")
print("The N = 1 approximation is so far off because our approximaton is essencially assuming that the function is linear between 0 and 2.")
print()

#B1

# I spent an egregious amount of time trying to get this function to work like I wanted it to so hopefully you think it is as cool as I do.
# It should be generalizable to virtually any function f, interval a to b, and number of trapezoids N.
# Define a functon to outaput a visual representation of the trapezoidal approximation

def trap_plot(f, a, b, N):
    x_plot = np.arange(a,b,.05) # create an pseudo-continuous array of x values between a and b to give the illusion of plotting a continuous function
    y_plot = f(x_plot) # run this pseudo-continuous array through our function to get our y value array

    plt.plot(x_plot, y_plot, color = "black") # plot our function using these arrays

    h = (b - a) / N # step size
    x_trap_plot = [] # create two blank lists which we will fill with pairs of x and y values that will act as the basis for the trapezoids that plt.fill_between will draw
    y_trap_plot = []

# you can definitely do this in one for loop but this way is more intitive to me

    for n in range(0, N): # for every trapezoid (number determined by N)
        x_pair = np.array([a + n * h, a + (n + 1) * h ]) # create an array of the x values where one of the trapezoids starts and ends
        x_trap_plot.append(x_pair) # append our blank list from above with this pair of x trapezoid boundary values
    x_trap_plot_array = np.array(x_trap_plot) # convert this list of pairs of trapezoid boundary values to an array

    for n in range(0, N): 
         y_pair = f(x_trap_plot_array[n]) # create an array of the y values corresponding to these x values by running the correspoding x value pair array through f
         y_trap_plot.append(y_pair) # append our blank y list from above with this y value pair
    y_trap_plot_array = np.array(y_trap_plot) # convert this list of y value pair arrays to an array

    for n in range(0, N): 
        plt.fill_between(x_trap_plot_array[n], y_trap_plot_array[n], alpha = .5) # iterate through the x pair array and y pair array and use the fill between command to draw trapezoids defined by correspoding pair values

    plt.title(f"Trapezoidal Approximation with {N} Steps") # title the plot
    plt.xlabel("x") # label the axis
    plt.ylabel("f(x)")

    return plt.show() # return the finished plot

trap_plot(f,0,2,4) # call our trap_plot function with N = 4

#B2

trap_plot(f,0,2,8) # call our trap_plot function with N = 8

print("result for B2: ") # pretty self-explanitory, print the answer to the question B2
print("I notice that as N increases, the error decreases.") 
print()

#C1

N_list = [10,20,40,80,160] # define a list of N values for our error table
error_table_list = [] # create a blank list for our error table arrays
np.set_printoptions(suppress=True, precision=6) # set print options for the numpy array so that we dont deal with numbers in scientific notation

for N in N_list: # iterate through each N list value
    error_table_array = np.array([float(N), trapezoid(f,0,2,N), numerical_error(4.4, trapezoid(f,0,2,N)), percent_error(4.4, trapezoid(f,0,2,N))]) # For each value create an array consisting of [N, approximation value, numerical error, percent error]
    error_table_list.append(error_table_array) # Append these arrays to our empty list

error_table_format =np.vstack(error_table_list) # Turn the now full list into an array and organize it vertically by column using np.vstack

print("Results for C1: ") # print this table to answer question C1
print(f"format: [N  ,  Estimate  ,  Numerical Error  ,  Percent Error]")
print(error_table_format)
print()

#C2

print("Results for C2: ") # Print our answer to question C2
print("From this table, I notice that, when N doubles, the error between our estimate and the true value of the integral shrinks by a factor of approximately 4.")
print()

#C3

N_plot_array = np.arange(1,200, dtype=int) # again, create a pseudo-contintuous array of N values for our error plot
measured_value_list = [] # create a blank list for our error values

for n in N_plot_array: # iterate through every value in our pseudo-continuous array
    measured_value_list.append(trapezoid(f,0,2,n)) # compute the trapezoidal approximation value for each value of N in this array and append it to the empty list
measured_value_array = np.array(measured_value_list) # turn our list of approximation values into an array

error_plot_array = numerical_error(np.full(len(N_plot_array), 4.4), measured_value_array) # create an array of the error values for each trapezoidal approximation at some specific N

plt.plot(N_plot_array, error_plot_array) # Plot N vs Error
plt.xscale("log", base=2) # set x axis to scale by log base 2
plt.xlabel("Value of N") # label x axis
plt.yscale("log", base=2) # set y axis to scale by log base 2
plt.ylabel("Approximation Error") # label y axis
plt.title("Log-Log (Base 2) Plot of N vs Trapezoidal Approximation Error") # title plot
plt.show() # show the plot

approximate_slope = (log(error_plot_array[-1] / error_plot_array[0], 2)) / (log(N_plot_array[-1] / N_plot_array[0], 2)) # find the approximate slope of the log-log graph by taking the log2(rise) / log2(run) of the first and last coordinates becasue it is approximately linear

print("Results for C3: ") # print the results to question C3
print(f"The slope of the log-log plot is {approximate_slope} (approximately -2)") # Use a formatted string to display our approximate slope value (the difference between which and the expected value can be blamed on floating point errors)
print()

print("Reflection: ") # print reflection 
print("The trapezoidal rule is a numerical method that approximates the integral, or area under the curve, of some function over some interval. It does this by breaking the area under the curve into trapezoids and summing their known areas. To break the area up into trapezoids, the approximation assumes that the function is linear over some step size h (a value dependent on the number of trapezoids used, N), an assumption which is only true when h is of a an infinitely small length dh. Therefore, as h becomes smaller (as N gets larger), it approaches this differential length and is therefore more accurate in it's approximation of the area under the curve.")