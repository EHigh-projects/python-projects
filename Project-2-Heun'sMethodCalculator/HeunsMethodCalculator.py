from math import * 

def function(x,y):
    result = 2*x - y
    return result 

def heun(x_initial, y_intial, x_final, number_of_iterations):

    h = (x_final - x_initial) / number_of_iterations
    result = [(x_initial, y_intial)]

    for n in range(0, number_of_iterations):

        a = function(x_initial, y_intial)
        prediction_y =  h * a + y_intial
        b = function(x_initial + h, prediction_y)
        true_y = y_intial + .5 * (a + b) * h

        result.append((x_initial + h, true_y, a, prediction_y, b))

        x_initial = x_initial + h 
        y_intial = true_y

    return result

print(heun(0,2,1,5))

# flow
# take x and y value - find slope - predict using slope - take slope of prediction point - average slopes and find next y value.