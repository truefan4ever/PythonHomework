import math
from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """
    This class inherit abstract class GeometricFigure from task 5.1.
    Instance of this class is initialized by radius.
    It redefins methods of a parent class to calculate square and
    perimeter of the circle."""

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_square(self):
        pass


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        print('Perimeter is:', 2 * math.pi * self.radius)

    def calculate_square(self):
        print('Square is:', math.pi * self.radius * self.radius)


circle = Circle(4)
circle.calculate_perimeter()
circle.calculate_square()
