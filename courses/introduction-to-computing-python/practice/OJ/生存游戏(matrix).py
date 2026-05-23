import copy
n,m=map(int,input().split())
cells=[[0]*(m+2)]
for i in range(0,n):
    cells.append([0]+list(map(int,input().split()))+[0])
cells.append([0]*(m+2))
cells_new=[row[:] for row in cells]
for i in range(1,n+1):
    for j in range(1,m+1):
        cell=cells[i-1][j-1]+cells[i-1][j]+cells[i-1][j+1]+cells[i][j-1]+cells[i][j+1]+cells[i+1][j-1]+cells[i+1][j]+cells[i+1][j+1]
        if cells[i][j]==1 and cell==2:
            cells_new[i][j]=1
        elif cell==3:
            cells_new[i][j]=1
        else:
            cells_new[i][j] = 0
for i in range(1,n+1):
    print(*cells_new[i][1:-1])
