from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    """
    This function gets a num as an argument
    and returns a dict, where the key is a
    number and the value is the square of that num."""

    res_dict = {i: i ** 2 for i in range(1, num + 1)}
    return res_dict


if __name__ == '__main__':
    print(generate_squares(5))
