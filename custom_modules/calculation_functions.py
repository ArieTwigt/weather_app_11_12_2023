import math

def calc_circle(diameter: float, rounding: int=1) -> float:
    '''
    Calculates the size of a circle    
    '''

    radius = diameter / 2
    size = (radius ** 2) * math.pi
    size_rounded = round(size, rounding)

    return size_rounded