def DtoB(n):
    ans = ""
    while(n!=0):
        m = n&1
        if(m==0):
            ans = ans + "0"
        else:
            ans = ans + "1"
        n=n>>1
    return int(ans[::-1])

print(DtoB(65535))