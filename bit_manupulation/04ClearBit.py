def Clear(n,pos):
    return (n & ~(1<<pos))

print(Clear(5, 0))