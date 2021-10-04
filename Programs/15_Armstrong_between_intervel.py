n = int(input("Enter a First Positive Intervel: "))
n1 = int(input("Enter a Second Positive Intervel: "))

for i in range (n,n1+1):
    j=0
    n2=i
    while(n2!=0):
        j+=1
        n2//=10
    arm=0
    n2=i
    while(n2!=0):
        rem = n2 % 10
        arm = arm + (rem ** j)
        n2//=10

    if(arm == i):
        print(i)
    