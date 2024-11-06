# Adrianna Francone
# UWYO COSC 1010
# 11/6/2024
# Lab 08
# Lab Section:15
# Sources, people worked with, help given to: Lecture Slides



# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
bad = "bad"

def int_or_float(value):
    i = value.count(".")
    if "-" in value:
        value = value.replace("-","")
        if i > 1:
            return bad
        elif "." in value:
            if (value.replace(".","")).isdigit():
                value = -float(value)
                return value
            else:
                return bad
        else:
            if value.isdigit():
                value = -int(value)
                return value
            else:
                return bad
    else: 
        if i > 1:
            return bad
        elif "." in value:
            if (value.replace(".","")).isdigit():
                value = float(value)
                return value
            else:
                return bad
        else:
            if value.isdigit():
                value = int(value)
                return value  
            else:
                return bad 


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def point_slope_eq(m,b,x_upper,x_lower):
    x_values = list(range(x_lower,x_upper+1))
    y_values = m*(x_values)
    y_values = [x+b for x in y_values]
    print(y_values)
    return y_values
    


while True:
    exit = "exit"
    m = input("Please input integar value for m or exit to end program: ")
    if m.upper()==exit.upper():
        break
    else:
        m = int_or_float(m)
        if m == bad:
            print("Please enter valid values")
            continue
    b = input("Please input integar value for b or exit to end program: ")
    if b.upper()==exit.upper():
        break
    else:
        b = int_or_float(b)
        if b == bad:
            print("Please enter valid values")
            continue
    x_lower = input("Please input integar value for x_lower or exit to end program: ")
    if x_lower.upper()==exit.upper():
        break
    else:
        x_lower = int_or_float(x_lower)
        if x_lower == bad:
            print("Please enter valid values")
            continue
    x_upper = input("Please input integar value for upper bound for x or exit to end program: ")
    if x_upper.upper()==exit.upper():
        break
    else:
        x_upper = int_or_float(x_upper)
        if x_upper == bad:
            print("Please enter valid values")
            continue
    if x_upper > x_lower:
        y_values = point_slope_eq(m,b,x_upper,x_lower)
    else: 
        print("Please enter valid values")


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def sq_root(a,b,c):
    quad_input = (b**2)-(4*a*c)
    if quad_input < 0:
        return bad
    else:
        sqroot = (quad_input**(1/2))
        return sqroot

def solve_quad(a,b,c):
    sqroot = sq_root(a,b,c)
    if sqroot == bad:
        return bad
    else:
        x1 = (-b + sqroot)/(2*a)
        x2 = (-b - sqroot)/(2*a)
        return [x1,x2]

while bad:
    exit = "exit"
    a = input("Please input integar value for a or exit to end program: ")
    if a.upper()==exit.upper():
        break
    else:
        a = int_or_float(a)
        if a == bad:
            print("Please enter valid values")
            continue
    b = input("Please input integar value for b or exit to end program: ")
    if b.upper()==exit.upper():
        break
    else:
        b = int_or_float(b)
        if b == bad:
            print("Please enter valid values")
            continue
    c = input("Please input integar value for c or exit to end program: ")
    if c.upper()==exit.upper():
        break
    else:
        c = int_or_float(c)
        if c == bad:
            print("Please enter valid values")
            continue
    x = solve_quad(a,b,c)
    if x == bad:
        print("Null")
        print("Please enter valid values")
        continue
    else:
        print(f"First root is {x[0]}, second root is {x[1]}")

