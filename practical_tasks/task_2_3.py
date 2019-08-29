from typing import Dict


def count_letters(string: str) -> Dict[str, int]:
    """
    This function gets a str as an argument and
    returns a dict, where the key is a letter and
    the value is the number of their occurence."""

    res_dict = {}

    for letter in string:
        if letter in res_dict:
            res_dict[letter] += 1
        else:
            res_dict[letter] = 1

    return res_dict


if __name__ == '__main__':
    print(count_letters("stringsample"))
