def reverse(n):
    re = 0
    while(n!=0):
        rem = n%10
        re = re * 10 + rem
        n//=10
    return re

print(reverse(123005))
