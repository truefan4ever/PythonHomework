def get_longest_word(string: str) -> str:
    """
    This function gets a string and returns
    the longest word in it. The word can contain
    any symbols except whitespaces. If there are
    multiple longest words in the string with a
    same length returs the word that occures first."""
    words = string.split(' ')
    word_length = []

    for word in words:
        word_length.append(len(word))

    longest_word = words[word_length.index(max(word_length))]

    return longest_word


if __name__ == '__main__':
    string = "Python is simple and effective!"
    # string = 'Any pythonista like namespaces a lot.'
    result = get_longest_word(string)
    print(result)
