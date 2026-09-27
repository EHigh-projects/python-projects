# To begin, I import all of the functions from python's built-in math library by passing in an asterisk after the import command.

from math import * 

# I then define all of the neccesary fundamental veriables of the schrodinger equation using input() objects for added functionality. 
# Examining the problem, the most fundamental variables, and therefore those that I should define first, include mass, initial_kinetic_energy, h_bar, and V (the energy of the potential barrier). 
# According to wikipedia, h_bar is a the reduced planck constant, or rather the planck constant reduced by a factor of 2pi.
# Because python code runs line-by-line, it makes the most sense to define any constants first before using any more complicated tools like the input object. 
# Additionally, I must be sure to use the float() object to convert our inputs to numerical values because, by default, input values are strings.

h_bar = (6.62607015 * 10 ** (-34)) / (2 * pi)
mass = float(input("Particle mass (in kg) = "))
initial_kinetic_energy = float(input("Initial kinetic energy of the particle (in eV)= "))
potential_energy_barrier = float(input("Potential energy barrier (in eV) = "))

# Here I will add an if statement to check if the particle's initial kinetic energy is greater than the potential energy barrier. 
# this is important because, according to wikepedia, if the particle wave has less kinetic energy than the potential energy barrier, instead of reflecting off of or transmitting over the barrier, the particle wave has a non-zero chance to tunnel through the barrier. 
# Contextually, this means that this program will not work if initial_kinetic_energy is less than potential_energy_barrier.
# Additionally, this makes sense mathematically, as by the definition of k_2, initial_kinetic_energy cannot be less than potential_energy_barrier because that would result in a negative argument inside of a square root.
# I use the exit function to immediately stop the program to prevent the negative square root argument error from occuring in the event that the potential energy barrier is greater than the initial kinetic energy of the particle.

if initial_kinetic_energy < potential_energy_barrier:
    print("Error: kinetic energy of particle wave is less than potential energy barrier.")
    exit()

# Now that I have defined the most fundamental variables, I can now define was k_1 and k_2 are.

k_1 = sqrt((2 * mass * initial_kinetic_energy) / (h_bar))
k_2 = sqrt((2 * mass * (initial_kinetic_energy - potential_energy_barrier)) / h_bar)

# Now that I have defined all of the variables neccesary to write the equations that will give us our probability values, I am now free to code said equations.
# I also define a variable to be the sum of the two properties, as this will be helpful later. 

transmission_probability = (4 * k_1 * k_2) / ((k_1 + k_2) ** 2)
reflection_probability = ((k_1 - k_2) / (k_1 + k_2)) ** 2
probability_sum = transmission_probability + reflection_probability

# Then, all that is left to do is to output both probabilities using the print() object
# Before I output the probabilities, however, I will add an if condition to check if the probabilites add to the expected value of 1.
# Additionally, I will use the round() object in order to help avoid any floating point errors. 
# I decided to round to a margin of 10 decimal places because floating point errors are usually incredibly small, so, realistically, any error should be discarded while any significany deviation from the expecetd value should trigger the else statement and print our error message.

if round(probability_sum, 10) == 1: 
    print("Transmission probability = ", transmission_probability)
    print("Reflection probability = ", reflection_probability)
else:
    print("Error: probabilities do not add to 1")
