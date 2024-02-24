def place_center(size1:tuple[int|float, int|float], size2:tuple[int|float, int|float]) -> tuple[int, int]:
    '''Get the top-left cords to place object of size2 onto size1'''
    return size1[0] // 2 - size2[0] // 2, size1[1] // 2 - size2[1] // 2

