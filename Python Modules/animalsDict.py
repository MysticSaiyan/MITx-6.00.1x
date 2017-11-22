animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    tempList = []
    count = 0
    for key in aDict:
        tempList = aDict[key]
        for i in tempList:
            count += 1
    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    tempList = []
    counter = 0
    test = 0
    for key in aDict:
        tempList = aDict[key]
        for i in tempList:
            counter += 1
        if counter > test:
            big = key
            test = counter
    return big
            
        
        
