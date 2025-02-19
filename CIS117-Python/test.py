import math

def hypotenuse(side1, side2):
    """Returns the length of the hypotenuse of a right triangle
    with legs x and y.
    """
    return math.sqrt(side1**2 + side2**2)

def cube(x):
    """Returns the cube of x."""
    return x**3

def square(x):
    """Returns the square of x."""
    return x**2

if __name__ == "main":
    print("Hypotenuse of a triangle with legs 3 and 4:", hypotenuse(3, 4))
    print("Cube of 3:", cube(3))



