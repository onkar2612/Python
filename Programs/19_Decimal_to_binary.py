n = int(input("Enter a Decimal number: "))
n1 = n
List1 = []
while(n1!=0):
    rem = n1%2
    List1.append(rem)
    n1//=2

List1.reverse()
print("Decimal number ",n," Is in Binary is:")
for i in List1:
    print(i,end=" ")
