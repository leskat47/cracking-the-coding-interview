def is_one_away(str1, str2):
    """ Determine if two strings are one modification away from being the same

    >>> is_one_away("catty", "kitty")
    False

    >>> is_one_away("grey", "gray")
    True

    >>> is_one_away("road", "rod")
    True

    >>> is_one_away("toad", "toady")
    True

    """

    # Fail fast: words must be within 1 letter length of each other
    # If len == len: check for one difference
    # Else: Check for all the same, but one extra letter

    if str1 == str2:
        return True

    changed = False
    iter1 = 0
    iter2 = 0
    str1_end = len(str1)
    str2_end = len(str2)

    while iter1 < str1_end and iter2 < str2_end:
        if str1[iter1] != str2[iter2]:
            if changed:
                return False
            changed = True
            if iter1 < len(str1) - 2 and str1[iter1 + 1] == str2[iter2]:
                iter1 += 1
            elif iter2 < len(str2) - 2 and str2[iter2 + 1] == str1[iter1]:
                iter2 += 1
        iter1 += 1
        iter2 += 1

    if str2_end - iter2 > 1 or str1_end - iter1 > 1:
        return False

    return True
