def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))

def Towers(num, fr, to, spare):
    if num == 1:
        printMove(fr, to)
    else:
        Towers(num-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(num-1, spare, to, fr)



print(Towers(10,'P1','P2','P3'))
