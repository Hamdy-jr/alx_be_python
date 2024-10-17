import math

# Base Class - Shape
class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # List of shapes (Rectangle and Circle) demonstrating polymorphism
    shapes = [
        Rectangle(10, 5),  # Rectangle with length 10 and width 5
        Circle(7)  # Circle with radius 7
    ]

    # Iterate through the shapes and print their respective areas
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
