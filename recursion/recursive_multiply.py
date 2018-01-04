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


def mult_helper(multiplier, num_to_multiply, memo):
    """ Return sum of num_to_multiply value smaller number of times """

    # The following could be written in a more concise way, but was intended to
    # be more step-wise and explanatory for presentation.

    # Base cases:
    if multiplier == 0:
        return 0
    if multiplier == 1:
        return num_to_multiply

    # Check our cache: if we've already solved for multiplier, return value from memo.
    if memo.get(multiplier):
        return memo[multiplier]

    # Break multiplier in two. It may be uneven
    first_half = multiplier / 2
    second_half = multiplier - first_half

    # Recurse on first half
    first_mult = mult_helper(first_half, num_to_multiply, memo)

    # If the halves were not equal recurse second half,
    # else second recursion is same as first
    if first_half != second_half:
        second_mult = mult_helper(second_half, num_to_multiply, memo)
    else:
        second_mult = first_mult

    # Update cache with our result
    memo[multiplier] = first_mult + second_mult

    # Return result
    return memo[multiplier]
