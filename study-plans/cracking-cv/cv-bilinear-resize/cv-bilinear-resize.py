import math

def bilinear_resize(image: list, new_h: int, new_w: int) -> list:
    """
    Returns the new_h-by-new_w resized list of floats, rounded to four decimals.
    """
    H = len(image)
    W = len(image[0])


    fh = (H-1)/(new_h-1) if new_h > 1 else 0
    fw = (W-1)/(new_w-1) if new_w > 1 else 0

    
    newim = []
    
    newim = [[0] * new_w for _ in range(new_h)]

    for i in range(new_h):
        for j in range(new_w):
            y = i * fh
            x = j * fw
            y0 = math.floor(y)
            x0 = math.floor(x)

            y1 = min(y0+1, H-1)
            x1 = min(x0+1, W-1)

            dx = x - x0
            dy = y - y0


                
            top = (1 - dx) * image[y0][x0] + dx * image[y0][x1]
            bottom = (1-dx) * image[y1][x0] + dx * image[y1][x1]

            val = (1-dy) * top + dy * bottom
            
            newim[i][j] = float(val)

    return newim
            
            