def avg_pool_2d(image: list, kernel_size: int, stride: int) -> list:
    """
    Returns the average-pooled 2D list of floats, rounded to four decimals.
    """
    k = kernel_size
    s = stride
    H = len(image)
    W = len(image[0])
    h = (H-k)//s + 1
    w = (W-k)//s + 1
    out = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            v = sum(v for row in image[i*s: i*s + k] for v in row[j*s : j*s+k])
            a = v/ (k**2)

            out[i][j] = round(float(a), 4)

    return out
            