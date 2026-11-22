def max_pool_2d(image: list, kernel_size: int, stride: int) -> list:
    """
    Returns the max-pooled 2D list of floats, rounded to four decimals.
    """
    s = stride
    H = len(image)
    W = len(image[0])
    h = (H - kernel_size)//s + 1
    w = (W - kernel_size)//s + 1
    out = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):

            v = max(v for row in image[i*s: i*s+ kernel_size] for v in row[j*s: j*s + kernel_size])
            
            out[i][j] = round(float(v), 4)
    return out