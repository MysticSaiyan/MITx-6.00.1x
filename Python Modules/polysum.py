
def polysum(n,s):
    '''
    calculates area and perimeter of polygon
    of n sides of s length each and adds 
    area and perimeter squared
    '''
    
    import math                                   # importing the math module
    area = (0.25*n*(s**2))/(math.tan(math.pi/n))  #calculated area
    perimeter = n*s                               #calculated perimeter
    return round(area + perimeter**2, 4)          #calculated polysum