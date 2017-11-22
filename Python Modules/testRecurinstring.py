def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    aStr = ''.join(sorted(aStr))
    if aStr == '':   #base case
        return False
    if len(aStr) == 1 or char == aStr[len(aStr)//2]: #base cases
        return char == aStr[len(aStr)//2]
    else:         #recursion
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[0:len(aStr)//2])
        else:
            return isIn(char, aStr[(len(aStr)//2)+1:len(aStr)])
        
        
