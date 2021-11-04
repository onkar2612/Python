def IsPowerOf2(n):
    return not((n & (n-1))!=0)

print(IsPowerOf2(64))