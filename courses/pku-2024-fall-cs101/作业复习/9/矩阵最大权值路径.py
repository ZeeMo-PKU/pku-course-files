# #n*m的矩阵
# #dfs
# #quan_now 不含x，y点
# #quan_new含
# n,m=map(int,input().split())
# ditu=[[0]]
# for i in range(0,n):
#     ditu.append([0]+list(map(int,input().split()))+[0])
#
# fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
# quan_max=-float('inf')
# lujing_best=[]
# def dfs(x,y,quan_now,lujing_now):
#     global quan_max
#     global lujing_best
#
#     lujing_now.append((x,y))
#     quan_new=quan_now+ditu[x][y]
#     if x==n and y==m and quan_new>quan_max:
#         lujing_best=lujing_now.copy()#包括（n，m）
#         quan_max=quan_new
#         return
#     huisu=ditu[x][y]
#     ditu[x][y]=float('-inf')
#     for (dx,dy) in fangxiang:
#         if 0<x+dx<=n and 0<y+dy<=m and ditu[x+dx][y+dy]!=float('-inf'):
#
#             dfs(x+dx,y+dy,quan_new,lujing_now)
#             lujing_now.pop(-1)
#     ditu[x][y]=huisu
# dfs(1,1,0,[])
# for (a,b) in lujing_best:
#     print(a,b)


