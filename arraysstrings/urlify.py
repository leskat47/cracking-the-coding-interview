def URLify(s_arr):
    """ Given a string replace blank spaces with %20 (in place, so use a list)

    >>> s_arr = ['a', ' ', ' ', 'b', ' ', 'c' , ' ']
    >>> URLify(s_arr)
    >>> s_arr
    ['a', '%20', 'b', '%20', 'c']

    """

    start = 0
    end = 0
    stop = len(s_arr) - 1

    while end < stop:
        if s_arr[end] == ' ':
            end += 1
            if end == stop:
                s_arr[start:] = []
        else:
            if start != end:
                s_arr[start:end] = ['%20']
                end = end - start + 1
                start = end
            else:
                start = end + 1
                end += 1
