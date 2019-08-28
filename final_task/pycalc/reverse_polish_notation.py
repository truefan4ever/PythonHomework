from . import config


def transformation(splitted_str: list) -> list:
    """
    This function gets a splitted list and and according to the
    algorithm of reverse polish notation converts it. Returns the
    converted list.
    """
    out = []
    stack = []

    for item in splitted_str:
        if type(item) == float or type(item) == list:
            out.append(item)
        elif item in config.FUNCTIONS_AND_OPERATORS:
            while True:
                if not stack or stack[-1] == "(":
                    stack.append(item)
                    break
                else:
                    if (config.FUNCTIONS_AND_OPERATORS[item][0] >
                            config.FUNCTIONS_AND_OPERATORS[stack[-1]][0]):
                        stack.append(item)
                        break
                    elif item == '^' and stack[-1] == '^':
                        stack.append(item)
                        break
                    else:
                        out.append(stack.pop())
        elif item in "()":
            if item == "(":
                stack.append(item)
            elif item == ")":
                while stack[-1] != "(":
                    out.append(stack.pop())
                stack.pop()
        elif item == ',':
            while stack[-1] != '(':
                out.append(stack.pop())
    while stack:
        out.append(stack.pop())
    return out
