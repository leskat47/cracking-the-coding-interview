
def is_unique1(test_str):
    """
    >>> is_unique1("abc")
    True
    >>> is_unique1("abca")
    False
    """

    letters = set()
    for char in test_str:
        if char in letters:
            return False
        else:
            letters.add(char)
    return True

def is_unique2(test_str):
    """
    >>> is_unique2("abc")
    True
    >>> is_unique2("abca")
    False

    """

    chars = set(test_str)

    if len(test_str) == len(chars):
        return True

    return False

def is_unique3(test_str):
    """ Is every character in a string unique? (No other data structures)

    >>> is_unique3("abc")
    True
    >>> is_unique3("abca")
    False

    """

    for i in range(len(test_str) - 1):
        for j in range(i+1, len(test_str)):
            if test_str[i] == test_str[j]:
                return False
    return True


def ctci_is_unique(test_str):
    """ Is every character in a string unique? (No other data structures)

    >>> ctci_is_unique("abc")
    True
    >>> ctci_is_unique("abca")
    False

    """

    checker = 0
    for char in test_str:
        if checker & (1 << ord(char)):
            return False
        checker |= (1 << ord(char))
    return True
