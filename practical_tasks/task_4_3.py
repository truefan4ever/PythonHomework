from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """
    This class inherit abstract class GeometricFigure from task 5.1.
    Instance of this class is initialized by length and width.
    It redefines methods of parent class to calculate square and
    perimeter of the rectangle. It has method for calculating length
    of its diagonals and method which checks if given rectangle fits
    in a circle of a given radius."""

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_square(self):
        pass


class Rectangle(GeometricFigure):
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def calculate_perimeter(self):
        print('Perimeter is:', 2 * (self.width + self.length))

    def calculate_square(self):
        print('Square is:', self.width * self.length)

    def calculate_diagonal(self):
        diagonal = (self.length**2 + self.width**2)**0.5
        print("Diagonal of the rectangle is:", diagonal)

    def check_fitting(self):
        if self.radius * 2 == (self.length**2 + self.width**2)**0.5:
            print("This rectangle fits the circle with radius:", self.radius)
        else:
            print("This rectangle doesn`t fit the circle.")


rectangle = Rectangle(4, 3, 3)
rectangle.calculate_square()
rectangle.calculate_perimeter()
rectangle.calculate_diagonal()
rectangle.check_fitting()
