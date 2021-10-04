def fac(n):
    if(n<=1):
        return n
    else:
        return n*fac(n-1)

n = int(input("Enter a number: "))
print("The factorial of ",n," is ",fac(n))
    