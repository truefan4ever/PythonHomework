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
                try:
                    # checking if the function has 2 arguments
                    config.FUNCTIONS_AND_OPERATORS[item][1](1, 1)
                    second_argument, first_argument = stack.pop(), stack.pop()
                    args = [first_argument, second_argument]
                except TypeError:
                    argument = stack.pop()
                    args = [argument]
            try:
                stack.append(config.FUNCTIONS_AND_OPERATORS[item][1](*args))
            except ZeroDivisionError:
                raise ValueError('ERROR: you should not devide by zero')
            except ValueError:
                raise ValueError("ERROR: check the data")
            except TypeError:
                raise ValueError("ERROR :check the data")

    return stack[-1]
