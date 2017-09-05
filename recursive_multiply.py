def mult(x, y):
    """ Return the product of two numbers """

    if y == 1:
        return x

    return mult(x, y - 1) + x

# ///////////////////////////////////////////
# Better solution


def mult2(x, y):
    """ Return product of two numbers """
    if x < y:
        smaller, bigger = x, y
    else:
        smaller, bigger = y, x

    # Dictionary for memoization
    memo = {}
    return mult_helper(smaller, bigger, memo)


def mult_helper(smaller, bigger, memo):
    """ Return sum of bigger value smaller number of times """

    # The following could be written in a more concise way, but was intended to
    # be more step-wise and explanatory for presentation.

    # Base cases:
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    # If we've already solved for smaller, return value from memo.
    if memo.get(smaller):
        return memo[smaller]

    # Break smaller in two. 
    first_half = smaller / 2
    second_half = smaller - first_half

    # Recurse on first half
    first_mult = mult_helper(first_half, bigger, memo)

    # If the halves were not equal recurse second half,
    # else second recursion is same as first
    if first_half != second_half:
        second_mult = mult_helper(second_half, bigger, memo)
    else:
        second_mult = first_mult

    # Add smaller to memo dictionary with result as the value
    memo[smaller] = first_mult + second_mult

    # Return result
    return memo[smaller]
