def rgb_to_grayscale(image: list) -> list:
    """
    Returns the H-by-W grayscale list of floats, rounded to four decimals.
    """

    l = []
    for i in range(len(image)):
        tl = []
        for j in range(len(image[i])):
            tl.append(0.299 * image[i][j][0] + 0.587* image[i][j][1] + 0.114* image[i][j][2])

        l.append(tl)

    return l