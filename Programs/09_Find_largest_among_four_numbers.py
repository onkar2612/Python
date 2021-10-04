def Largest(n,n1,n2,n3):
    if(n>n1 and n>n2 and n>n3):
        return n
    elif(n1>n2 and n1>n3):
        return n1
    elif(n2>n3):
        return n2
    else:
        return n3


print("Largest number is ",Largest(1,5,16,9))
print("Largest number is ",Largest(1,24,6,9))
print("Largest number is ",Largest(85,5,16,9))
print("Largest number is ",Largest(85,5,16,999))