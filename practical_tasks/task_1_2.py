def checking(string):
    """
    This function checks if a string
    is a palindrome or not."""
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    string = "madam"
    result = checking(string)
    if result:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")
