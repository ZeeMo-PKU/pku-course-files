from collections import deque
n,m=map(int,input().split())
ditu=[]
for i in range(0,n):
    ditu.append(list(map(int,input().split())))
num=0

fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
def bfs(x1,y1):
    A=deque([(x1,y1)])
    while A:
        (x,y)=A.popleft()
        for dx,dy in fangxiang:
            if 0<=x+dx<n and 0<=y+dy<m and ditu[dx+x][dy+y]==1:
                A.append((x+dx,y+dy))
                ditu[x+dx][y+dy]=0

for i in range(0,n):
    for j in range(0,m):
        if ditu[i][j]==1:
            ditu[i][j]=0
            num+=1
            bfs(i,j)
print(num)
# print(ditu)
