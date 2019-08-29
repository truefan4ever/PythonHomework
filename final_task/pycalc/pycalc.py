from .cli import parser
from .errors import errors
from .splitting import string_splitting
from .reverse_polish_notation import transformation
from .calculating import calculate


def main():
    """
    This function calls all functions for calculating.
    """
    print(calculate(transformation(errors(string_splitting(parser())))))


def check_result(expression: str) -> float or bool:
    return(calculate(transformation(errors(string_splitting(expression)))))


if __name__ == '__main__':
    main()
