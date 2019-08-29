from typing import Optional
from typing import Set
import string


def test_1_1(*strings) -> Optional[Set[str]]:
    """
    This function gets a changeable number of strings
    and return characters that appear in all strings."""
    sets = [set(item) for item in strings]
    return sets[0].intersection(*sets[1:]) if sets else None


def test_1_2(*strings) -> Optional[Set[str]]:
    """
    This function gets a changeable number of strings and
    return characters that appear in at least one string."""
    sets = [set(item) for item in strings]
    return sets[0].union(*sets[1:]) if sets else None


def test_1_3(*strings) -> Optional[Set[str]]:
    """
    This function gets a changeable number of strings and
    return characters that appear at least in two strings."""
    if not strings:
        return None
    sets = [set(item) for item in strings]
    result = {}
    for item in sets:
        for char in item:
            result[char] = result.get(char, 0) + 1
    return {key for key in result if result[key] > 1}


def test_1_4(*strings) -> Optional[Set[str]]:
    """
    This function gets a changeable number of strings and return
    characters of alphabet, that were not used in any string."""
    if not strings:
        return None
    letters_set = set(string.ascii_lowercase)
    sets = [set(item) for item in strings]
    return letters_set.difference(sets[0].union(*sets[1:]))


if __name__ == '__main__':
    test_strings = []
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings))
