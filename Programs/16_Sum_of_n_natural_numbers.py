# Using recurssion
def sum(n):
    if (n==0):
        return n
    elif (n==1):
        return n
    else:
        return n+sum(n-1)

print(sum(4))

# n = int(input("Enter a number: "))
# sum = 0
# if(n==0):
#     print(n)
# elif(n==1):
#     print(n)
# else:
#     for i in range(1,n+1):
#         sum = sum + i
#     print(sum)