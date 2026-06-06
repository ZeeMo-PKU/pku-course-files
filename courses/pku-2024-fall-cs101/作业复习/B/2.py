import sys
from functools import lru_cache

sys.setrecursionlimit(100000000)


r,c=map(int,input().split())

ditu=[list(map(int,input().split())) for _ in range(0,r)]

dp=[[-1]*c for i in range(0,r)]

fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
@lru_cache
def dfs(x,y):
    if dp[x][y]>0:
        return
    for dx,dy in fangxiang:
        nx=x+dx
        ny=dy+y
        if 0<=nx<r and 0<=ny<c and ditu[nx][ny]<ditu[x][y]:

            if dp[nx][ny]==-1:
                dfs(nx,ny)
            dp[x][y]=max(dp[x][y],dp[nx][ny]+1)

    if dp[x][y]==-1:
        dp[x][y]=1

for i in range(0,r):
    for j in range(0,c):
        dfs(i,j)
out=0
for i in dp:
    out=max(out,max(i))

print(out)