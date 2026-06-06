# fangxiang={(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)}
# num=0
# def dfs(x,y):
#     global num
#     if ditu[x][y]=='W':
#         num+=1
#         ditu[x][y]='.'
#         for dx,dy in fangxiang:
#             nx=x+dx
#             ny=dy+y
#             dfs(nx,ny)
#     else:
#         return
#
#
# t=int(input())
# for i2 in range(0,t):
#     n,m=map(int,input().split())
#     ditu=[['.']*(m+2)]
#     for i in range(0,n):
#         ditu.append(['.']+list(input())+['.'])
#     ditu.append(['.']*(m+2))
#     ans=[]
#     # print(ditu)
#     for x in range(1,n+1):
#         for y in range(1,m+1):
#             if ditu[x][y]=='W':
#                 num=0
#                 dfs(x,y)
#                 ans.append(num)
#     if ans:
#         print(max(ans))
#     else:print(0)



# #dfs
# T=int(input())
#
#
# fangxiang={(-1,1),(-1,0),(-1,-1),
#            (0,1),(0,-1),
#            (1,1),(1,0),(1,-1)}
# ditu=[]
# num_new=0
# def dfs(x,y):
#     global num_new
#     if ditu[x][y]=='W':
#         num_new+=1
#         ditu[x][y]='.'
#         for dx,dy in fangxiang:
#             dfs(x+dx,y+dy)
#
# for i1 in range(0,T):
#     num_new=0
#     #N*M的矩阵
#     N,M=map(int,input().split())
#     ditu=[['.']*(M+2)]
#     for i in range(0,N):
#         ditu.append(['.']+list(input())+['.'])
#     ditu.append(['.']*(M+2))
#     num=0
#     for i in range(1,N+1):
#         for j in range(1,M+1):
#             num_new=0
#             dfs(i,j)
#             num=max(num,num_new)
#
#     print(num)
# # #bfs
# # from collections import deque
# #
# # T=int(input())
# # mianji_max=0
# #
# # fangxiang={(-1,1),(-1,0),(-1,-1),
# #            (0,1),(0,-1),
# #            (1,1),(1,0),(1,-1)}
# # ditu=[]
# # num_max=0
# # def bfs(x,y):
# #     global num_max
# #     A=deque([(x,y)])
# #     num=1
# #     seen={(x,y)}
# #     while A:
# #         (kx,ky)=A.popleft()
# #         for (dx,dy) in fangxiang:
# #             if (kx+dx,ky+dy) not in seen and ditu[kx+dx][ky+dy]=='W':
# #                 A.append((kx+dx,ky+dy))
# #                 num+=1
# #     num_max=max(num,num_max)
# #
# #
# #
# # for i1 in range(0,T):
# #     num_max=0
# #     #N*M的矩阵
# #     N,M=map(int,input().split())
# #     ditu=[['.']*(M+2)]
# #     for i in range(0,N):
# #         ditu.append(['.']+list(input())+['.'])
# #     ditu.append(['.']*(M+2))
# #     for i in range(1,N+1):
# #         for j in range(1,M+1):
# #             if ditu[i][j]=='W':
# #                 bfs(i,j)
# #     print(num_max)
# #bfs
# from collections import deque
#
# T=int(input())
# mianji_max=0
#
# fangxiang={(-1,1),(-1,0),(-1,-1),
#            (0,1),(0,-1),
#            (1,1),(1,0),(1,-1)}
# ditu=[]
# num_max=0
# def bfs(x,y):
#     global num_max
#     A=deque([(x,y)])
#     num=1
#     seen={(x,y)}
#     while A:
#         (kx,ky)=A.popleft()
#         for (dx,dy) in fangxiang:
#             if (kx+dx,ky+dy) not in seen and ditu[kx+dx][ky+dy]=='W':
#                 A.append((kx+dx,ky+dy))
#                 num+=1
#     num_max=max(num,num_max)
#
#
#
# for i1 in range(0,T):
#     num_max=0
#     #N*M的矩阵
#     N,M=map(int,input().split())
#     ditu=[['.']*(M+2)]
#     for i in range(0,N):
#         ditu.append(['.']+list(input())+['.'])
#     ditu.append(['.']*(M+2))
#     for i in range(1,N+1):
#         for j in range(1,M+1):
#             if ditu[i][j]=='W':
#                 bfs(i,j)
#     print(num_max)
from collections import deque


def bfs(ditu, x, y, N, M):
    A = deque([(x, y)])
    num = 1
    seen = {(x, y)}
    while A:
        (kx, ky) = A.popleft()
        ditu[kx][ky]='.'
        for (dx, dy) in fangxiang:
            nx, ny = kx + dx, ky + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in seen and ditu[nx][ny] == 'W':
                A.append((nx, ny))
                seen.add((nx, ny))
                num += 1
    return num


T = int(input())
fangxiang = {(-1, 1), (-1, 0), (-1, -1),
             (0, 1), (0, -1),
             (1, 1), (1, 0), (1, -1)}

for _ in range(T):
    N, M = map(int, input().split())
    ditu = [list(input().strip()) for _ in range(N)]

    max_area = 0
    for i in range(N):
        for j in range(M):
            if ditu[i][j] == 'W':
                area = bfs(ditu, i, j, N, M)
                max_area = max(max_area, area)

    print(max_area)