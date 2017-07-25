def search(lst, find):
    """Searches the given list for the given item using binary search. In
       this case, lst is a list which is sorted but, post-sort, has been
       rotated an arbitrary amount. Returns the index of the item if found,
       -1 otherwise.

       In order to have this run in log time, assume all elements are unique.

       For example:

       >>> search([5, 7, 8, 9, 1, 3, 4], 8)
       2

       >>> search([5, 7, 8, 9, 1, 3, 4], 10)
       -1

       >>> search([], 1)
       -1

       >>> search([2, 2, 2, 3, 4, 2], 3)
       3

    """
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (end + start) / 2

        if lst[mid] == find:
            return mid

        # left side is in order
        if lst[start] < lst[mid]:
            # it's on the left side - reset search to left side
            if find >= lst[start] and find < lst[mid]:
                end = mid - 1
            # it's on the right side - reset search to right side
            else:
                start = mid + 1

        # right side is in order
        elif lst[mid] < lst[end]:
            # it's on the right side
            if find > lst[mid] and find <= lst[end]:
                start = mid + 1
            # search left
            else:
                end = mid - 1

        # Check for a side that is all a repeated number
        # left side repeats, but right side doesn't
        elif lst[start] == lst[mid] and lst[mid] != lst[end]:
                start = mid + 1
        # right side repeats, but left side doesn't
        elif lst[mid] == lst[end] and lst[start] != lst[mid]:
                end = mid - 1
        # we have the same number on both ends and in center:
        elif lst[start] == lst[mid] == lst[end]:
            start = start + 1
            end = end - 1
        else:
            return -1

    return -1


def search_rotated(lst, find):
    """Searches the given list for the given item using a recursive binary 
       search. In this case, lst is a list which is sorted but, post-sort, has 
       been rotated an arbitrary amount. Returns the index of the item if found,
       -1 otherwise.

       In order to have this run in log time, assume all elements are unique.

       For example:

       >>> search_rotated([5, 7, 8, 9, 1, 3, 4], 8)
       2

       >>> search_rotated([5, 7, 8, 9, 1, 3, 4], 10)
       -1

       >>> search_rotated([], 1)
       -1

       >>> search_rotated([2, 2, 2, 3, 4, 2], 3)
       3

    """

    start = 0
    end = len(lst)-1

    def search_portion(start, end):
        """ Recursive search through binary search """

        if end < start:
            return -1

        mid = (end + start) / 2

        if lst[mid] == find:
            return mid

        # left side is in order
        if lst[start] < lst[mid]:
            # it's on the left side - reset search to left side
            if find >= lst[start] and find < lst[mid]:
                return search_portion(start, mid - 1)
            # it's on the right side - reset search to right side
            else:
                return search_portion(mid + 1, end)

        # right side is in order
        elif lst[mid] < lst[end]:
            # it's on the right side
            if find > lst[mid] and find <= lst[end]:
                return search_portion(mid + 1, end)
            # search left
            else:
                return search_portion(start, mid - 1)

        # Check for a side that is all a repeated number
        # left side repeats, but right side doesn't - search right
        elif lst[start] == lst[mid] and lst[mid] != lst[end]:
            return search_portion(mid + 1, end)
        # right side repeats, but left side doesn't - search left
        elif lst[mid] == lst[end] and lst[start] != lst[mid]:
            return search_portion(start, mid - 1)
        # we have the same number on both ends and in center - search both sides
        elif lst[start] == lst[mid] == lst[end]:
            # check left
            sub_result = search_portion(start, mid -1)
            if sub_result == -1:
                # check right
                return search_portion(mid +1, end)
            else:
                return sub_result
        return -1

    return search_portion(start, end)

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
