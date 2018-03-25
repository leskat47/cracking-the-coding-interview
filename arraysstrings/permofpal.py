def is_perm_of_pal(str):
    """ Determine if a string is a permutation of a palindrome

    >>> is_perm_of_pal("actt oca")
    True

    >>> is_perm_of_pal("act oca")
    False

    """

    odds = set()

    for letter in str:
        if letter in odds:
            odds.remove(letter)
        elif letter != " ":
            odds.add(letter)


    return len(odds) <= 1
