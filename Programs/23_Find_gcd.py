n = int(input("Enter a number: "))
n1 = int(input("Enter a second number: "))
for i in range(n,-1,-1):
    if(n%i==0 and n1%i==0):
        print(i)
        break