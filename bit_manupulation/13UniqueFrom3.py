arr = [10,34,22,67,22,34,10,10,34,22]
n=10
tn = 65535
tn1 =0
tn2 =0
for i in range(n):
    cwn=tn&arr[i]
    cwn1=tn1&arr[i]
    cwn2=tn2&arr[i]

    tn = tn & (~cwn)
    tn1 = tn1 |cwn

    tn1 = tn1 & (~cwn1)
    tn2 = tn2 |cwn1

    tn2 = tn2 & (~cwn2)
    tn = tn |cwn2

print(tn1)