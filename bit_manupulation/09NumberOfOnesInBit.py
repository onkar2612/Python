def bits(n):
    i=0
    while(n!=0):
        n2 = 1 & n
        if(n2!=0):
            i=i+1
        n = n>>1
    return i

print(bits(1999900000))