def need_to_change(num1,num2):
    n = num1 ^ num2
    i=0
    while(n!=0):
        n2 = 1 & n
        if(n2!=0):
            i=i+1
        n = n>>1
    return i

print(need_to_change(18, 29))