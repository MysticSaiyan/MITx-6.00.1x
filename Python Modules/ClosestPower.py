def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    test = num
    while True: 
        value = base**exp
        if abs(value-num) < test:
            test = abs(value-num)
            exp += 1
        else:
            break;
    return (exp-1)
        
        
        
    