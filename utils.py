def place_center(size1:tuple[int|float, int|float], size2:tuple[int|float, int|float]) -> tuple[int, int]:
    '''Get the top-left cords to place object of size2 onto size1'''
    return size1[0] // 2 - size2[0] // 2, size1[1] // 2 - size2[1] // 2

def vector_add(vec1:tuple[int|float, int|float], vec2:tuple[int|float, int|float]) -> tuple[int|float, int|float]:
    return vec1[0] + vec2[0], vec1[1] + vec2[1]

def vector_sub(vec1:tuple[int|float, int|float], vec2:tuple[int|float, int|float]) -> tuple[int|float, int|float]:
    return vec1[0] - vec2[0], vec1[1] - vec2[1]

def vector_opp(vec:tuple[int|float, int|float]) -> tuple[int|float, int|float]:
    return -vec[0], -vec[1]

