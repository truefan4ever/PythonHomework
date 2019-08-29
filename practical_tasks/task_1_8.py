from typing import List


def get_pairs(list_of_data: List[int]) -> List[tuple]:
    """
    This function gets a list of int and returns a list of
    tuples containing pairs of elements. Pairs should be
    formed as in the example. get_pairs([1, 2, 3, 8, 9])
    [(1, 2), (2, 3), (3, 8), (8, 9)]."""

    final_list = []

    if len(list_of_data) > 1:
        a = [[0] * 2 for i in range(len(list_of_data) - 1)]
        a[0][0] = list_of_data.pop(0)
        a[-1][-1] = list_of_data.pop(-1)

        for i in range(len(list_of_data)):
            a[i][1] = list_of_data[i]
            a[i + 1][0] = list_of_data[i]

        for i in a:
            item = tuple(i)
            final_list.append(item)

        return final_list
    else:
        return None


if __name__ == '__main__':
    list_of_data = [1, 2, 3, 8, 9]
    # list_of_data = [1]
    result = get_pairs(list_of_data)
    print(result)
