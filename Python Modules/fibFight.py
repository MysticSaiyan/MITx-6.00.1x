
def fib(x):
    global numFibCalls
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def fib_efficient(x, d):
    global numFibCalls
    numFibCalls += 1
    if x in d:
        return d[x]
    else:
        ans = fib_efficient(x-1,d) + fib_efficient(x-2, d)
        d[x] = ans
        return ans
d = {1:1, 2:1}

def superfib(x):
    p1=0
    p2=1
    while x>2:
        global numFibCalls
        numFibCalls += 1
        px = p1+p2
        p1 = p2
        p2 = px
        x -= 1
    return p2+p1


fibArg = 34

numFibCalls = 0
print(fib(fibArg))
print("No. of calls : " + str(numFibCalls))

numFibCalls = 0
print(fib_efficient(fibArg, d))
print("No. of calls : " + str(numFibCalls))

numFibCalls = 0
print(superfib(fibArg))
print("No. of calls : " + str(numFibCalls))













