def rotated_binary_search(lst, item):
    """Searches the given list for the given item using binary search. In
       this case, lst is a list which is sorted but, post-sort, has been
       rotated an arbitrary amount. Returns the index of the item if found,
       -1 otherwise.

       In order to have this run in log time, assume all elements are unique.

       For example:

       >>> rotated_binary_search([5, 7, 8, 9, 1, 3, 4], 8)
       2

       >>> rotated_binary_search([5, 7, 8, 9, 1, 3, 4], 10)
       -1

       >>> rotated_binary_search([], 1)
       -1

    """

    #define the initial bounds - in the form of indices - of our search
    #because this is our first pass, we're searching everything
    low = 0
    high = len(lst) - 1

    #keep searching until we either find the item or have nothing left to
    #search (meaning the interval in which we're searching has negative width)
    while low <= high:

        #compute the halfway point
        mid = (high + low) / 2

        #check the item at the center of our current search interval and return
        #its index if it's what we're looking for
        if lst[mid] == item:
            return mid

        #if we haven't found our item, we now have to contend with the fact
        #that our interval may contain the inflection point - the point where
        #the max is followed immediately by the min

        #however, since there's only one inflection point, only one half of our
        #interval can possibly contain it

        #there are a few possibilities:

        # a1) the item at mid is too high and the item at low is too low (or
        #equal to our item) => our item must be in the lefthand half

        # a2) the item at mid is too high and the item at low is *also* too
        #high => our item must be in the righthand half

        # b1) the item at mid is too low and the item at high is too high (or
        #equal to our item) => our item must be in the righthand half

        # b2) the item at mid is too low and the item at high is also too low
        # => our item must be in the lefthand half

        #therefore, we just need to figure out which of these scenarios we're
        #in and adjust our bound accordingly

        #options a1 and b2
        if ((lst[mid] > item and lst[low] <= item) or
            (lst[mid] < item and lst[high] < item)):
            #pick lefthand half
            high = mid - 1

        #options a2 and b1
        if ((lst[mid] > item and lst[low] > item) or
            (lst[mid] < item and lst[high >= item])):
            #pick righthand half
            low = mid + 1


    #if we've gotten to this point, it's because our while loop has finished
    #without having found (and returned the index of) our desired item
    #therefore, return -1 as a flag for "not found"
    return -1





if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED.\n")
