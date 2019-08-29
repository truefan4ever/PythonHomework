def replacing(string):
    """
    This function receives a string and replaces
    all " symbols with ' and vise versa."""
    print(string)
    if "'" in string:
        new_str = string.replace("'", "\"")
        return new_str
    elif "\"" in string:
        new_str = string.replace("\"", "'")
        return new_str


if __name__ == '__main__':
    string = "He said: \"I`m so tired!\""
    # string = "He said: 'I`m so tired!'"
    result = replacing(string)
    print(result)
