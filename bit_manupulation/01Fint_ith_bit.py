def Ith_Bit(n,pos):
    n1 = (n & (1<<pos))

    if(n1):
        return 1
    else:
        return 0

print(Ith_Bit(22, 3))