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

def URLify_2(s_arr):
    """ Given a string replace blank spaces with %20 (in place, so use a list)

    >>> s_arr = ['a', ' ', ' ', 'b', ' ', 'c' , ' ']
    >>> URLify_2(s_arr)
    >>> s_arr
    ['a', '%20', 'b', '%20', 'c']

    """

    left = len(s_arr) - 1
    right = len(s_arr) - 1

    for left in range(len(s_arr) - 1, -1, -1):
        if s_arr[left] == ' ':
            if right == len(s_arr) - 1:
                s_arr.pop()
                right -= 1
            if left == 0:
                s_arr[left:right + 1] = []
        else:
            if left != right:
                s_arr[left + 1:right + 1] = ['%20']
                right = left - 1
            else:
                right = right - 1
