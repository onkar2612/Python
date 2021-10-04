m=[[1,2],
[4,5],
[6,7]]

m2=[[1,2,3],
[4,5,6],
[7,8,3]]

m3=[[0,0],
[0,0],
[0,0]]

for i in range(len(m3)):
    for j in range(len(m3[0])):
        for k in range(len(m)):
            m3[i][j]+=m2[i][k]*m[k][j]

for r in m3:
    print(r)