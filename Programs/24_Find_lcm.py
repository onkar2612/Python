n = int(input("Enter a number: "))
n1 = int(input("Enter a second number: "))
n3 = max(n,n1)
while(True):
    if(n3 % n==0 and n3 % n1 == 0):
        print(n3)
        break
    n3+=1
