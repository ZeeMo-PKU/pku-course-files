#这是我的RE代码
# from collections import deque
# import sys
# fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
# def bfs(x,y,ditu,shuiyan):
#     H=ditu[x][y]
#     A=deque([(x,y)])
#     while A:
#         # print(A)
#         (x1,y1)=A.popleft()
#         shuiyan[x1][y1]=1
#         for dx,dy in fangxiang:
#             # print(x+dx,y+dy)
#             if 0<x1+dx<=N and 0<y1+dy<M+1 and shuiyan[x1+dx][y1+dy]==0:
#                 if x1+dx==kx and dy+y1==ky and H>ditu[kx][ky]:
#                     return True
#                 if ditu[x1+dx][y1+dy]<=H:
#                     A.append((x1+dx,y1+dy))
#     return False
#
# a=[0]+list(sys.stdin.read().split('\n'))
# #print(a)
# num=1
# K=int(a[num])
#
#
# for i in range(0,K):
#     num+=1
#     M,N=map(int,a[num].split())
#     ditu=[[0]]
#     for j in range(0,M):
#         num+=1
#         ditu.append([0]+list(map(int,a[num].split())))
#     shuiyan = [[0] * (N + 1) for _ in range(M + 1)]
#     num+=1
#     kx,ky=map(int,a[num].split())
#     num+=1
#     P=int(a[num])
#     aq=0
#     for o in range(0,P):
#         num+=1
#         x,y=map(int,a[num].split())
#         op=bfs(x,y,ditu,shuiyan)
#
#         if not op:
#             aq+=1
#
#
#     if aq==P:
#         print('No')
#     else:
#         print('Yes')

from collections import deque
import sys
MAXN=1111
def bfs(x,y):
    global slb,mat
    q=deque([(x,y)])
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 1<=nx<=m and 1<=ny<=n \
            and mat[nx][ny]<mat[x][y]:
                q.append((nx,ny))
                mat[nx][ny]=mat[x][y]
                if (nx,ny)==slb:
                    return('Yes')
    return ('No')
lines=list(sys.stdin.read().split())

t=int(lines[0])
id=1
for _ in range(t):
    m,n=map(int,(lines[id],lines[id+1]))
    mat=[[MAXN]*(n+2)]
    id+=2
    for i in range(m):
        mat.append([MAXN]+list(map(int,lines[id:id+n]))+[MAXN])
        id+=n
    mat.append([MAXN]*(n+2))
    slb=(int(lines[id]),int(lines[id+1]))
    id+=2
    k=int(lines[id])
    id+=1
    H2O=[]
    for i in range(k):
        H2O.append((int(lines[id]),int(lines[id+1])))
        id+=2
    for h20 in H2O:
        ans=bfs(h20[0],h20[1])
        if ans=='Yes':
            print(ans)
            break
    else:print('No')