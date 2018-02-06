def paint_fill(image, col, row, color, orig_color):
    if image[col][row] != orig_color:
        return
    if row < 0 or row >= len(image) or col < 0 or col > len(image[0]):
        return
    image[col][row] = color

    paint_fill(image, col - 1, row, color, orig_color)
    paint_fill(image, col + 1, row, color, orig_color)
    paint_fill(image, col, row - 1, color, orig_color)
    paint_fill(image, col, row + 1, color, orig_color)

    return  
