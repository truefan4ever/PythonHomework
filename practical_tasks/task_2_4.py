from typing import Dict


def combine_dicts(*args):
    """
    This function gets a changeable number of dictionaries
    (keys - letters, values - numbers) and combines them
    into one dictionary. Dict values should be summarized
    in case of identical keys."""

    res_dict = {}
    for dictionary in args:
        for key in dictionary:
            try:
                res_dict[key] += dictionary[key]
            except KeyError:
                res_dict[key] = dictionary[key]

    return res_dict


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))
