n,m=map(int,input().split())
map1=[[0]*(m+2)]
for i in range(0,n):
    map1.append([0]+list(map(int,input().split()))+[0])
map1.append([0]*(m+2))
C=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if map1[i][j]==1:
            C+=4
            C-=(map1[i-1][j]+map1[i+1][j]+map1[i][j+1]+map1[i][j-1])
print(C)