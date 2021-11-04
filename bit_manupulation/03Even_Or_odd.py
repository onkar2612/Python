def EorO(n):
    n1 = n & 1
    if(n1):
        return f"{n} Is odd number"
    else:
        return f"{n} Is even number"

print(EorO(15))