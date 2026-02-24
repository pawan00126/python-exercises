# Level 1: The Basics (Input & Output)These focus on the standard 

# def name(parameters): structure and the return statement.

# The Greeting Machine: Write a function called greet_user that takes a name as an argument and returns a string like "Hello, [name]! Welcome back."

def greet_user(name: str):
    return f"Hello, {name}! Welcome back."

print(greet_user('Pawan'))



# The Multiplier: Create a function multiply that takes two numbers and returns their product.
def multiply(a:int, b:int):
    return a*b

print(multiply(3,5))


import math
# Area Finder: Write a function circle_area that takes the radius as an input and returns the area.Hint: Use the formula $A = \pi r^2$. You can use 3.14 or import math.
def circle_area(rad:float):
    return round(math.pi*rad*rad, 3)


print(circle_area(1))



