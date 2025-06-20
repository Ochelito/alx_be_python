import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.") # indicating that derived classes need to override this method.
    

"""You're calculating area inside __init__, but __init__ is not meant to return values.

You haven’t overridden the area() method in the derived classes (Rectangle, Circle), which is the whole point of Shape.area().

In Circle, you're using ^ (bitwise XOR) instead of ** (exponentiation).

math module is used, but it's not imported."""

    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        result = self.length*self.width
        return result
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi*self.radius ** 2
        return result
    