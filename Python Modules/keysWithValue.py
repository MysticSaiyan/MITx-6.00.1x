def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keyList = []
    for key in aDict:
        if aDict[key] == target:
            keyList.append(key)
    keyList.sort()
    return keyList


