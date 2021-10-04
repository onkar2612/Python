l1 = [x for x in input().split(",")]
l2 = [x for x in input().split(",")]
s1=set()
s2=set()
for i in l1:
    s1.add(int(i))
for i in l2:
    s2.add(int(i))

print(s1)
print(s2)


print("Union of set is ",s1 or s2)
print("Intersection of set is ",s1 and s2)
print("Difference of set is ",s1 - s2)

