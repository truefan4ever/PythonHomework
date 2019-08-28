import re
import math
from .errors import spaces_between_operators
from . import config


def string_splitting(string: str) -> list:
    """
    This function gets an expression string and splits it by element.
    Converts all numbers to float, deletes spaces between elements,
    converts the expression to standart. Returns splitted list.
    """
    splitted_str = re.split("([/\*\-\+\^%>=<\(\)!,\s])", string)
    help_list = []
    OPERATORS = ("(", ",", "*", "/", "^", "//", "%",
                 ">", ">=", "<", "<=", "==", "!=")

    for index, value in enumerate(splitted_str):
        if value == '':
            splitted_str.pop(index)

    spaces_between_operators(splitted_str)

    for index, value in enumerate(splitted_str):
        if value == ' ':
            splitted_str.pop(index)

    for index, value in enumerate(splitted_str):
        if (value == "/" and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "/"):
            splitted_str[index + 1] = '//'
            splitted_str.pop(index)
        elif (value == ">" and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "="):
            splitted_str[index + 1] = '>='
            splitted_str.pop(index)
        elif (value == "<" and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "="):
            splitted_str[index + 1] = '<='
            splitted_str.pop(index)
        elif (value == "=" and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "="):
            splitted_str[index + 1] = '=='
            splitted_str.pop(index)
        elif (value == "!" and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "="):
            splitted_str[index + 1] = '!='
            splitted_str.pop(index)
        elif value in config.CONSTANTS:
            splitted_str[index] = str(config.CONSTANTS[value])

    for index, value in enumerate(splitted_str):
        if '.' in value:
            splitted_str[index] = float(value)
        elif value.isdigit():
            splitted_str[index] = float(value)
        elif value == 'inf' or value == 'nan':
            splitted_str[index] = float(value)
    while True:
        for index, value in enumerate(splitted_str):
            if (value == '-' and index != len(splitted_str) - 1 and
                    splitted_str[index + 1] == '-'):
                splitted_str[index + 1] = '+'
                splitted_str.pop(index)

            elif (value == '-' and index != len(splitted_str) - 1 and
                    splitted_str[index + 1] == '+'):
                splitted_str[index + 1] = '-'
                splitted_str.pop(index)

            elif (value == '+' and index != len(splitted_str) - 1 and
                    splitted_str[index + 1] == '-'):
                splitted_str.pop(index)

            elif (value == '+' and index != len(splitted_str) - 1 and
                    splitted_str[index + 1] == '+'):
                splitted_str[index + 1] = "+"
                splitted_str.pop(index)

        help_list.append(splitted_str.copy())

        if len(help_list) > 1 and help_list[-1] == help_list[-2]:
            break
    for index, value in enumerate(splitted_str):
        if (value in OPERATORS and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "-" and
                type(splitted_str[index + 2]) == float):
            splitted_str[index + 2] = float('-' + str(splitted_str[index + 2]))
            splitted_str.pop(index + 1)

        elif ((value == "-" and index == 0) and
                index != len(splitted_str) - 1 and
                type(splitted_str[index + 1]) == float):
            splitted_str[index + 1] = float('-' + str(splitted_str[index + 1]))
            splitted_str.pop(index)

        elif (value in OPERATORS and index != len(splitted_str) - 1 and
                splitted_str[index + 1] == "-" and
                splitted_str[index + 2] in config.FUNCTIONS):
            splitted_str[index + 1] = 'neg'
        elif ((value == "-" and index == 0) and
                index != len(splitted_str) - 1 and
                splitted_str[index + 1] in config.FUNCTIONS):
            splitted_str[index] = 'neg'

    if 'log' in splitted_str:
        for index, value in enumerate(splitted_str):
            if value == 'log' and splitted_str[index + 1] == "(":
                first_arg = index + 2
            elif value == ")":
                last_arg = index
        list_of_args = splitted_str[first_arg:last_arg]

        if "," in list_of_args:
            config.FLAG_LOG = 1
        else:
            config.FLAG_LOG = 0

    if 'round' in splitted_str:
        for index, value in enumerate(splitted_str):
            if value == 'round' and splitted_str[index + 1] == "(":
                first_arg = index + 2
            elif value == ")":
                last_arg = index
        list_of_args = splitted_str[first_arg:last_arg]

        if "," in list_of_args:
            config.FLAG_ROUND = 1
        else:
            config.FLAG_ROUND = 0

    if 'fsum' in splitted_str:
        for index, value in enumerate(splitted_str):
            if value == 'fsum' and splitted_str[index + 1] == "(":
                first_num = index + 2
            elif value == ")":
                last_num = index

        list_of_nums = splitted_str[first_num:last_num]

        for index, value in enumerate(list_of_nums):
            if value == ',':
                list_of_nums.pop(index)

        new_list = splitted_str[:first_num]
        new_list.append(list_of_nums)
        new_list += splitted_str[last_num:]
        return new_list
    else:
        return splitted_str
