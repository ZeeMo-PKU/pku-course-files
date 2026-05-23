def dfs(x,y,jingkuang,leixing):
    fangxiang={(1,0),(0,1),(0,-1),(-1,0)}
    if jingkuang[x][y]==leixing:
        jingkuang[x][y] ='#'
        for (a1,a2) in fangxiang:
            if jingkuang[x+a1][y+a2]==leixing:
                dfs(x+a1,y+a2,jingkuang,leixing)
k=int(input())
for i in range(0,k):
    num_r=0
    num_b=0
    n=int(input())
    jingkuang = [['#']*(n+2)]
    for j in range(0,n):
        jingkuang.append(['#']+list(input())+['#'])
    jingkuang.append(['#']*(n+2))
    for i1 in range(1,n+1):
        for j1 in range(1,n+1):
            if jingkuang[i1][j1]=='r':
                num_r+=1
                dfs(i1,j1,jingkuang,'r')
            elif jingkuang[i1][j1]=='b':
                num_b+=1
                dfs(i1,j1,jingkuang,'b')
    print(num_r,num_b)
#bfs
from collections import deque
k=int(input())
fangxiang={(1,0),(0,1),(0,-1),(-1,0)}
for i in range(0,k):
    num_r=0
    num_b=0
    n=int(input())
    jingkuang = [['#']*(n+2)]
    for j in range(0,n):
        jingkuang.append(['#']+list(input())+['#'])
    jingkuang.append(['#']*(n+2))
    for i1 in range(1,n+1):
        for j1 in range(1,n+1):
            if jingkuang[i1][j1] == 'r':
                num_r += 1
                bfs(i1,j1,jingkuang,'r')
            elif jingkuang[i1][j1] == 'b':
                num_b += 1
                bfs(i1,j1,jingkuang,'b')
    print(num_r,num_b)






