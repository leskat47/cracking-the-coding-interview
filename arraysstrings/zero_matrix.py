def zero_lines(mtx):
    """ If there is a zero in the matrix, make all items in its row and column
        zero

        >>> mtx = [[1, 2, 4, 0, 5],
        ...        [3, 4, 5, 6, 7],
        ...        [3, 0, 5, 6, 7],
        ...        [3, 4, 5, 6, 7]]
        >>> zero_lines(mtx)
        [[0, 0, 0, 0, 0], [3, 0, 5, 0, 7], [0, 0, 0, 0, 0], [3, 0, 5, 0, 7]]

    """

    # traverse matrix, track zero locations
    row_locations = set()
    col_locations = set()
    for r in range(len(mtx)):
        for c in range(len(mtx[0])):
            if mtx[r][c] == 0:
                row_locations.add(r)
                col_locations.add(c)

    # clear rows with zeros
    clear_row = [0 for i in range(len(mtx[0]))]
    for row in row_locations:
        mtx[row] = clear_row

    # set of row locations not yet flipped
    row_items_left = set(range(len(mtx[0]) - 1)) - row_locations

    # replace columns
    for row in row_items_left:
        for col in col_locations:
            mtx[row][col] = 0

    return mtx
