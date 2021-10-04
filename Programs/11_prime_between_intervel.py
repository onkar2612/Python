n = int(input("Enter a first intervel: "))
n1 = int(input("Enter a second intervel: "))
print("Prime number between intervel are: ")
for i in range(n,n1+1):
    flag = True
    if(i==1):
        flag = False      
    for j in range(2,int((i/2)+1)):        
        if(i%j==0):
            flag = False      
    if(flag):
        print(i)