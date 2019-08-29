from typing import List


def split_by_index(string: str, indexes: List[int]) -> List[str]:
    """
    This function gets a string and a list of indexes
    and than splits the string by the indexes."""
    final_list = []
    new_str = ''
    if max(indexes) > len(string):
        final_list.append(string)
        return final_list

    else:
        a = [[0] * 2 for i in range(len(indexes) + 1)]
        a[0][0] = 0
        a[-1][-1] = len(string)

        for i in range(len(indexes)):
            a[i][1] = indexes[i]
            a[i + 1][0] = indexes[i]

        for i in a:
            start = i[0]
            stop = i[1]
            final_list.append(string[start:stop])

        return final_list


if __name__ == '__main__':
    string = "pythoniscool,isn`tit?"
    indexes = [6, 8, 12, 13, 18]
    result = split_by_index(string, indexes)
    print(result)
