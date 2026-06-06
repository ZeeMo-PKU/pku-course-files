from collections import deque
from collections import defaultdict
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
d=[[-1,0],[1,0],[0,1],[0,-1]]
v={}
v=defaultdict(lambda:float("inf"))
def bfs(x1,y1,x2,y2):
    q=deque()
    q.append((x1,y1,x2,y2,0))
    v[(x1,y1,x2,y2)]=0

    while q:
        x,y,z,w,t=q.popleft()

        if lst[x][y]==9 or lst[z][w]==9:
            return "yes"
        for dx,dy in d:
            nx1,ny1,nx2,ny2=x+dx,y+dy,z+dx,w+dy
            if nx1 in range(n) and ny1 in range(n) and nx2 in range(n) and ny2 in range(n) and lst[nx1][ny1]!=1 and lst[nx2][ny2]!=1 and v[(x,y,z,w)]+1<v[(nx1,ny1,nx2,ny2)]:
                q.append((nx1,ny1,nx2,ny2,v[(x,y,z,w)]+1))
                v[(nx1,ny1,nx2,ny2)]=v[(x, y, z, w)] + 1

    return "no"
for i in range(n):
    for j in range(n):
        if lst[i][j]==5:
            lst[i][j]=0
            x1,y1=i,j
            break
for i in range(n):
    for j in range(n):
        if lst[i][j]==5:

            x2,y2=i,j
            break
print(lst)
print(x1,x2,y1,y2)
l=bfs(x1,y1,x2,y2)
print(l)