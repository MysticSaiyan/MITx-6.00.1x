

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    value = 1
    while exp > 0:
        if exp == 0:
            base =  1
        else:
            value *= base
        exp -= 1
    return value
    
        