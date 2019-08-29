from . import config


def empty_error(splitted_str: list) -> list:
    """
    This function gets a splitted list and checks if it`s not empty.
    If it`s empty prints the error and finishs the execution.
    Otherwise returns the splitted list.
    """
    if not splitted_str:
        raise ValueError('ERROR: string should not be empty.')
    else:
        return splitted_str


def spaces_between_operators(splitted_str: list) -> list:
    """
    This function gets a splitted list and checks the spaces between
    operators. If there are spaces, prints the error and finishs the
    execution. Otherwise returns the splitted list.
    """
    OPERATORS = ('>', '<', '/', '!', '=', '*')
    for index, value in enumerate(splitted_str):
        if (value in OPERATORS and index != len(splitted_str) - 1 and
            index + 1 != len(splitted_str) - 1 and
                splitted_str[index + 1] == " " and
                splitted_str[index + 2] in OPERATORS):
            raise ValueError("ERROR: it should not be a "
                             "space between operators")


def brackets_error(splitted_str: list) -> list:
    """
    This function gets a splitted list and counts the brackets.
    If the number of open brackets not equal to the number of close
    brackets, prints the error and finishs the execution.
    Otherwise returns the splitted list.
    """
    if splitted_str.count('(') != splitted_str.count(')'):
        raise ValueError("ERROR: brackets are not balanced")
    else:
        return splitted_str


def unknown_function_error(splitted_str: list) -> list:
    """
    This function gets a splitted list and checks the existence of a
    function. If this function not exists, prints the error and finishs
    the execution. Otherwise returns the splitted list.
    """
    for item in splitted_str:
        if (type(item) != float and item not in config.FUNCTIONS and
                item not in "()"):
            raise ValueError(f"ERROR: unknown function '{item}'")
        else:
            return splitted_str


def operands_error(splitted_str: list) -> list:
    """
    This function gets a splitted list and checks if the expression is
    correct. If it is not correct, prints the error and finishs the
    execution. Otherwise returns the splitted list.
    """
    COMPARISON = ('>', '<', '>=', '<=', '==', '!=')
    ARITHMETIC = ('-', '+', '*', '/', '//', '%', '^')

    for index, value in enumerate(splitted_str):
        if (type(value) == float and index != len(splitted_str) - 1 and
                type(splitted_str[index + 1]) == float):
            raise ValueError("ERROR: operator must be "
                             "between two operands")
    if len(splitted_str) == 2:
        if type(splitted_str[0]) == float and splitted_str[1] in ARITHMETIC:
            raise ValueError("ERROR: arithmetic operator must be "
                             "between two operands")
        elif (splitted_str[0] in ('*', '/', '//', '%', '^') and
                type(splitted_str[1]) == float):
            raise ValueError("ERROR: arithmetic operator must be "
                             "between two operands")
        elif splitted_str[0] in COMPARISON and type(splitted_str[1]) == float:
            raise ValueError("ERROR: comparison operator must be "
                             "between two operands")
        elif type(splitted_str[0]) == float and splitted_str[1] in COMPARISON:
            raise ValueError("ERROR: comparison operator must be "
                             "between two operands")
        elif splitted_str[0] in COMPARISON and splitted_str[1] in COMPARISON:
            raise ValueError("ERROR: comparison operator must be "
                             "between two operands")
        else:
            return splitted_str
    elif len(splitted_str) == 1:
        if splitted_str[0] in config.FUNCTIONS_AND_OPERATORS:
            raise ValueError("ERROR: operator must be between "
                             "two operands or func(args)")
        else:
            return splitted_str
    else:
        return splitted_str


def arguments_error(splitted_str: list) -> list:
    """
    This function gets a splitted list and checks the number of
    fuction`s arguments. If this number is bigger or lower than the
    number of argumets, prints the error and finishs the execution.
    Otherwise returns the splitted list.
    """
    FUNC_NAME = ''
    FLAG = False
    COUNTER_ARGS = 0
    for item in splitted_str:
        if type(item) == str and item in config.FUNCTIONS:
            FLAG = True
    if FLAG:
        for index, value in enumerate(splitted_str):
            if (type(value) == str and value in config.FUNCTIONS and
                    splitted_str[index + 1] == "("):
                first_arg = index + 2
                FUNC_NAME = value
            elif value == ")":
                last_arg = index

        list_of_args = splitted_str[first_arg:last_arg]

        if FUNC_NAME == 'log' or FUNC_NAME == 'round':
            if ',' in list_of_args:
                num_of_comma = list_of_args.count(',')
                if num_of_comma == 1:
                    if list_of_args[0] == ',' and len(list_of_args) >= 2:
                        raise ValueError(f"ERROR: {FUNC_NAME} missed "
                                         "the first argument")
                    elif list_of_args[-1] == ',' and len(list_of_args) >= 2:
                        raise ValueError(f"ERROR: {FUNC_NAME} missed "
                                         "the second argument")
                    elif list_of_args[0] == ',' and len(list_of_args) == 1:
                        raise ValueError(f"ERROR: {FUNC_NAME} missed "
                                         "two arguments")
                    else:
                        return splitted_str

                else:
                    raise ValueError(f"ERROR: {FUNC_NAME} takes exactly 1 "
                                     "or 2 arguments")
            else:
                if not list_of_args:
                    raise ValueError(f'ERROR: {FUNC_NAME} takes exactly 1 '
                                     'or 2 arguments(0 given)')
                else:
                    return splitted_str

        else:
            try:
                # checking if the function has 2 arguments
                config.FUNCTIONS[FUNC_NAME][1](1, 1)
                num_of_args = 2
            except TypeError:
                num_of_args = 1

            if ',' in list_of_args:
                num_of_comma = list_of_args.count(',')

                if num_of_comma == 1:
                    if list_of_args[0] == ',' and len(list_of_args) >= 2:
                        raise ValueError(f"ERROR: {FUNC_NAME} missed the "
                                         "first argument")
                    elif list_of_args[-1] == ',' and len(list_of_args) >= 2:
                        raise ValueError(f"ERROR: {FUNC_NAME} missed the "
                                         "second argument")
                    elif list_of_args[0] == ',' and len(list_of_args) == 1:
                        raise ValueError(f"ERROR: {FUNC_NAME} missed two "
                                         "arguments")
                    else:
                        COUNTER_ARGS = 2
                        if COUNTER_ARGS != num_of_args:
                            raise ValueError(f"ERROR: {FUNC_NAME} takes "
                                             f"exactly {num_of_args} "
                                             f"argument(s) ({COUNTER_ARGS} "
                                             "given)")
                        else:
                            return splitted_str

                else:
                    raise ValueError(f"ERROR: {FUNC_NAME} takes exactly "
                                     f"{num_of_args} argument(s)")

            else:
                if not list_of_args:
                    raise ValueError(f'ERROR: {FUNC_NAME} takes exactly '
                                     f'{num_of_args} argument(s) (0 given)')
                else:
                    COUNTER_ARGS = 1
                    if COUNTER_ARGS != num_of_args:
                        raise ValueError(f"ERROR: {FUNC_NAME} takes exactly "
                                         f"{num_of_args} argument(s) "
                                         f"({COUNTER_ARGS} given)")
                    else:
                        return splitted_str

    else:
        return splitted_str


def errors(splitted_str: list) -> list:
    """
    This function is calling functions from this file.
    """
    return(arguments_error(operands_error(unknown_function_error(
        brackets_error(empty_error(splitted_str))))))
