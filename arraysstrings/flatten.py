def flatten(lst):
    """ Flatten a multidimensional array.

        >>> flatten([1, 2, [3, 4], [5, [6, 7]]])
        [1, 2, 3, 4, 5, 6, 7]
    """

    result = []

    for item in lst:
        if type(item) == list:
            fl = flatten(item)
            result.extend(fl)
        else:
            result.append(item)

    return result
