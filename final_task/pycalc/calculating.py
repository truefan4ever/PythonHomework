from inspect import signature
from . import config


def calculate(reverse_polish_notation: list) -> str:
    """
    This function gets the list converted to the reverse polish
    notation and calculates the expression. Returns string value.
    """
    stack = []

    for item in reverse_polish_notation:
        if type(item) == float or type(item) == list:
            stack.append(item)
        elif item in config.FUNCTIONS_AND_OPERATORS:
            if item == 'log':
                if config.FLAG_LOG:
                    second_argument, first_argument = stack.pop(), stack.pop()
                    args = [first_argument, second_argument]
                else:
                    argument = stack.pop()
                    args = [argument]
            elif item == 'round':
                if config.FLAG_ROUND:
                    second_argument, first_argument = stack.pop(), stack.pop()
                    args = [first_argument, int(second_argument)]
                else:
                    argument = stack.pop()
                    args = [argument]
            else:
                sig = signature(config.FUNCTIONS_AND_OPERATORS[item][1])
                params = sig.parameters
                num_of_args = len(params)
                if num_of_args == 1:
                    argument = stack.pop()
                    args = [argument]
                elif num_of_args == 2:
                    second_argument, first_argument = stack.pop(), stack.pop()
                    args = [first_argument, second_argument]
            try:
                stack.append(config.FUNCTIONS_AND_OPERATORS[item][1](*args))
            except ZeroDivisionError:
                print('ERROR: you should not devide by zero')
                exit(1)
            except ValueError:
                print("ERROR: check the data")
                exit(1)

    return str(stack[-1])
