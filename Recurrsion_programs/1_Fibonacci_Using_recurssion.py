def febonacci(n):
    if n<=1:
        return n
    else:
        return febonacci(n-1)+febonacci(n-2)

Terms = int(input("Enter a terms: "))

if(Terms<=0):
    print("Please enter positive number")

else:
    for i in range(Terms):
        print(febonacci(i))