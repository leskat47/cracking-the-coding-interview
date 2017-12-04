def is_permutation1(str1, str2):
    """ Are two strings permutations of one another
    nlog(n) solution

    >>> is_permutation1('abcda', 'bcdaa')
    True

    >>> is_permutation1('abcba', 'bcdaa')
    False
    """

    if sorted(list(str1)) == sorted(list(str2)):
        return True
    return False


def is_permutation2(str1, str2):
    """ Are two strings permutations of one another
    nlog(n) solution

    >>> is_permutation1('abcda', 'bcdaa')
    True

    >>> is_permutation1('abcba', 'bcdaa')
    False
    """

    if len(str1) != len(str2):
        return False

    letters = {}
    for char in str1:
        letters[char] == letters.get(char, 0) + 1

    for char in str2:
        if letters.get(char) > 0:
            letters[char] -= 1
        elif letters.get(char) <= 0:
            return False

    return True
