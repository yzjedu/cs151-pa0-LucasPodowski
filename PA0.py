# Solves functions for a degree of derivative and/or integral.

# Imports library to solve integrals and derivatives.
import sympy as sp

# Defines variables.
integral = 0
derivative = 0
degree = 0

# Prompts user to input type of problem to solve.
solve_type = str(input("Would you like to solve an integral, derivative, or both? ")).lower()

# Prompts user to input what degree and accounts for wrong answers.
if solve_type == 'derivative' or solve_type == 'both':
    degree = int(input("What degree of derivative? "))
elif solve_type == 'integral':
    print(end='')
else:
    print('Try again, enter integral, derivative or both!')
    quit()

# Prompts user to input hte variable to solve for in the function.
variable = input("Input one variable you want to solve for in your function: ")

# Establishes the variable for sympy
variable = sp.symbols(str(variable))

# Prompts user to input function.
function = input(f'Input a function f({variable}) to solve. Use ** before exponents. f({variable}) = ')

# Solves functions for derivative and integral
if solve_type == 'integral':
    integral = sp.integrate(function, variable)
elif solve_type == 'derivative':
    derivative = sp.diff(function, variable, degree)
else:
    integral = sp.integrate(function, variable)
    derivative = sp.diff(function, variable, degree)


# Outputs the answer to the problem.
if solve_type == 'integral':
    print('The integral to your function is:', integral)
elif solve_type == 'derivative':
    print('The derivative to your function is:', derivative)
else:
    print('The integral to your function is:', integral)
    print('The derivative to your function is:', derivative)