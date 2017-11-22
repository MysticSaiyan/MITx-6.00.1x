def getSublists(L, n):
    subList = []
    for i in range(len(L)):
        if i+n <= len(L):
            testList = L[i:i+n]
            subList.append(testList)
        else:
            break;
    return subList
