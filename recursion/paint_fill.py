def paint_fill(image, col, row, color, orig_color):
    if image[row][col] != orig_color:
        return
    if row < 0 or row >= len(image) or col < 0 or col > len(image[0]):
        return
    image[row][col] = color

    paint_fill(image, col - 1, row, color, orig_color)
    paint_fill(image, col + 1, row, color, orig_color)
    paint_fill(image, col, row - 1, color, orig_color)
    paint_fill(image, col, row + 1, color, orig_color)

    return  


image = [[1, 3, 3, 4],
         [1, 2, 2, 4],
         [1, 2, 3, 4],
         [1, 2, 2, 4],
         [1, 2, 3, 4],
         [1, 0, 3, 4],
        ]

paint_fill(image, 1, 2, 7, 2)

for row in image:
    print row
