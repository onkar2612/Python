import math
Values = 10
n=int(input("Enter a number: "))
rais_to=list(map(lambda i: math.pow(n,i), range(Values)))
for i in range (Values):
    print(n," Rais to ",i," = ",rais_to[i])