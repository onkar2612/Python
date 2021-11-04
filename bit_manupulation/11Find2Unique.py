arr=[10,20,34,43,10,67,20,43,67,87]
n = 10
xor = 0
for i in range(n):
    xor = xor^arr[i]
rsbm= xor & (-xor)
y=0
x=0
for i in range(n):
    if((arr[i]&rsbm)==0):
        x=x^arr[i]
    else:
        y=y^arr[i]

print(x," ",y)
