# Using recurssion
'''def fac(n):
    if(n<=0):
        return 0
    if(n==1):
        return 1
    else:
        return n*fac(n-1)

if __name__=="__main__":
    print(fac(5)) '''

n = int(input("Enter a number: "))
fac = 1
for i in range(1,n+1):
    fac = fac * i
print(fac)