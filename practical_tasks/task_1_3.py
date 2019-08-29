def splitting(string: str, separator: str):
    """
    This function gets string and splits it."""

    final_list = []
    index_list = []

    if separator in string:
        for ind, val in enumerate(string):
            if val == separator:
                index_list.append(ind)

        b = [[0] * 2 for i in range(len(index_list) + 1)]
        b[0][0] = 0
        b[-1][-1] = len(string)

        for i in range(len(index_list)):
            b[i][1] = index_list[i]
            b[i + 1][0] = index_list[i] + 1

        for i in b:
            start = i[0]
            stop = i[1]
            final_list.append(string[start:stop])

        return final_list

    else:
        return None


if __name__ == '__main__':
    string = "ABRA$CADABRA"
    separator = '$'
    print(splitting(string, separator))
