def setSort(L):
    for i in range(len(L)-1):
        print(L)
        minIndex = i
        minValue = L[i]
        j = i+1
        while j < len(L):
            if minValue > L[j]:
                minIndex = j
                minValue = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp

test = [1,5,3,8,9,4,7,2]