def Change_Bit(n,pos):
    sc = ((1<<pos)&n)
    ans = 0
    if(sc==0):
        ans = (n | (1<<pos))
    else:
        ans =  (n & ~(1<<pos))
    return ans
    
print(Change_Bit(10, 3))