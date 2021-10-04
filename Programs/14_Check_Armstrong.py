n = int(input("Enter a Positive number: "))
n1 = n
i=0
while(n1!=0):
    i+=1
    n1//=10
arm=0
n1=n
while(n1!=0):
    rem = n1 % 10
    arm = arm + (rem ** i)
    n1//=10

if(arm == n):
    print(n," Is a armstrong number")
else:
    print(n," Is not armstrong number")