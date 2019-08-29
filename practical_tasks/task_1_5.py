from typing import Tuple


def get_digits(num: int) -> Tuple[int]:
    """
    This function gets a num and adds
    every digit of it into the tuple."""

    res = tuple(int(i) for i in str(num))
    return res


if __name__ == '__main__':
    num = 87178291199
    result = get_digits(num)
    print(result)
