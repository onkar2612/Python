m=[[1,2,3],
[4,5,6],
[7,8,3]]

m2=[[1,2,3],
[4,5,6],
[7,8,3]]

m3=[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range (len(m)):
    for j in range (len(m[0])):
        m3[i][j]=m[i][j]+m2[i][j]


for r in m3:
    print(r)