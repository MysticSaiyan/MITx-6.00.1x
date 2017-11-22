
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    gcd = 0
    if a < b:
        test = a
    else:
        test = b
    while test > 0:
        if a%test == 0 and b%test == 0:
            gcd = test
            break
        else:
            test -= 1
    return gcd
