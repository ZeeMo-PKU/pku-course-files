#dfs
import sys
sys.setrecursionlimit(1e9)
count=0
def dfs(x,y,tiandi):
    fangxiang={(-1,-1),(0,-1),(0,1),(1,1),(1,-1),(1,0),(-1,0),(-1,1)}
    if tiandi[x][y]=='W':
        tiandi[x][y]='.'
        for (a1,a2) in fangxiang:
            dfs(x+a1,y+a2,tiandi)



N,M=map(int,input().split())
tiandi=[['.']*(M+2)]
for i in range(N):
    tiandi.append(['.']+list(input())+['.'])
tiandi.append(['.']*(M+2))
for i in range(1,N+1):
    for j in range(1,M+1):
        if tiandi[i][j] == 'W':
            count+=1
            dfs(i,j,tiandi)
print(count)
#bfs
from collections import deque
def bfs(x,y,tiandi):
    fangxiang={(-1,1),(-1,0),(-1,-1),
               (0,1),(0,-1),(1,1)
        ,(1,0),(1,-1)}
    seen={(x,y)}
    A=deque([(x,y)])
    while A:
        uuu=A.pop()
        for (a1,a2) in fangxiang:
            if tiandi[uuu[0]+a1][uuu[1]+a2]=='W':
                tiandi[uuu[0] + a1][uuu[1] + a2] ='.'
                if (uuu[0]+a1,uuu[1]+a2) not in seen:
                    A.append((uuu[0]+a1,uuu[1]+a2))
                    seen.add((uuu[0]+a1,uuu[1]+a2))


count=0
N,M=map(int,input().split())
tiandi=[['.']*(M+2)]
for i in range(N):
    tiandi.append(['.']+list(input())+['.'])
tiandi.append(['.']*(M+2))
for i in range(1,N+1):
    for j in range(1,M+1):
        if tiandi[i][j]=='W':
            count+=1
            bfs(i,j,tiandi)
print(count)

