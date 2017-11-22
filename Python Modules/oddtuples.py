def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    oddtup = ()
    for i in aTup[0::2]:
        oddtup = oddtup + (i,)
    return oddtup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple'))) 

        
