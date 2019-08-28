import argparse


def parser() -> str:
    """
    This function parses data from comand line.
    Returns the string expression.
    """
    parser = argparse.ArgumentParser(
        prog='pycalc',
        description='Pure-python command-line calculator')
    parser.add_argument('EXPRESSION',
                        type=str,
                        help='expression string to evaluate')

    args = parser.parse_args()

    return args.EXPRESSION
