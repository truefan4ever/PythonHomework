from typing import List


def foo(list_of_data: List[int]) -> List[int]:
    """
    This function gets a list of integers, returns
    a new list such that each element at index i of
    the new list is the product of all the numbers in
    the original array except the one at i."""

    final_list = []

    for i in range(len(list_of_data)):
        new_list = list_of_data.copy()
        new_list.pop(i)
        res = 1

        for i in new_list:
            res *= i
        final_list.append(res)

    return final_list


if __name__ == '__main__':
    list_of_data = [1, 2, 3, 4, 5]
    # list_of_data = [3, 2, 1]
    result = foo(list_of_data)
    print(result)
