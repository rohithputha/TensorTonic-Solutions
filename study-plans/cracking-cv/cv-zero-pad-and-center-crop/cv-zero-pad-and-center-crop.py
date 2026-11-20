def pad_image(image: list, pad:int)-> list:
    pad_h = [0.0]*len(image[0])
    for i in range(pad):
        image.append(pad_h)
        image.insert(0, pad_h)

    for i in range(len(image)):
        for p in range(pad):
            image[i].append(0.0)
            image[i].insert(0, 0.0)

    return image
def pad_and_center_crop(image: list, pad: int, crop_h: int, crop_w: int) -> list:
    """
    Returns the crop_h-by-crop_w list of floats, rounded to four decimals.
    """
    H = len(image)
    W = len(image[0])

    r0 = (H + 2*pad - crop_h)//2
    c0 = (W + 2*pad - crop_w)//2

    image = pad_image(image, pad)

    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = round(float(image[i][j]),4)            

    
    cim = []


    for i in range(r0, r0+crop_h):
        row = image[i]
        row = row[c0: c0+crop_w]
        cim.append(row)

    return cim
        