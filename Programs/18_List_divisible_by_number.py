print("Enter a list: ")
list1 = [i for i in input().split(",")]
n = int(input("Enter a nuber to divide: "))
for items in list1:
    if(int(items)%n==0):
        print(items)
