def sum_of_n(n):
    if(n<=1):
        return n
    else:
        return n+sum_of_n(n-1)

n = int(input("Enter a number: "))
print("The sum is ",sum_of_n(n))
    