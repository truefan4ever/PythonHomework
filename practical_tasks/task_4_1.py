from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """
    This class have abstract methods to calculate
    square and perimeter of the figure."""

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_square(self):
        pass


class Rectangle(GeometricFigure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        print('Perimeter is:', 2 * (self.width + self.length))

    def calculate_square(self):
        print('Square is:', self.width * self.length)


rectangle = Rectangle(4, 5)
rectangle.calculate_square()
rectangle.calculate_perimeter()
