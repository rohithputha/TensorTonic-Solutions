import numpy as np

def channel_statistics(batch: list) -> dict:
    """
    Returns mean and std lists of C floats in a dictionary, rounded to four decimals.
    """

    mu = []
    std = []
    l = len(batch) *len(batch[0]) * len(batch[0][0])

    channels = len(batch[0][0][0])
    for c in range(channels):
        m = 0
        s = 0
        for i in range(len(batch)):
            for j in range(len(batch[i])):
                for k in range(len(batch[i][j])):
                    m += batch[i][j][k][c]


        m = m/l 
        for i in range(len(batch)):
            for j in range(len(batch[i])):
                for k in range(len(batch[i][j])):
                    s += (batch[i][j][k][c] - m)**2
        s = (s/l)**0.5

        mu.append(m)
        std.append(s)

    return {
        "mean": mu,
        "std": std
    }