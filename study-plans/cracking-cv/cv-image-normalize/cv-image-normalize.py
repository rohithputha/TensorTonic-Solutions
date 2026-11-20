def normalize_image(image: list, mean: list, std: list) -> list:
    """
    Returns the normalized H-by-W-by-C list of floats, rounded to four decimals.
    """

    Y = image
    for i in range(len(image)):
        for j in range(len(image[i])):
            for  k in range(len(image[i][j])):
                Y[i][j][k] = (image[i][j][k]- mean[k])/std[k]

    return Y