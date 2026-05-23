# #dfs
# num=0
# nubiao=[1]
# fangxiang={(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,-1),(-2,1)}
# def dfs(x,y,ditu,step):
#     global num
#     if ditu[x][y]==0:
#         step+=1
#         if step==m*n:
#             num+=1
#             return
#         for (dx,dy) in fangxiang:
#             if 0<=x + dx<n and 0<=y+dy<m and 0 == ditu[x + dx][y + dy]:
#
#                 ditu[x][y]=1
#                 dfs(x+dx,y+dy,ditu,step)
#                 ditu[x][y]=0
#
# T=int(input())
# for i in range(0,T):
#     num=0
#     n,m,x,y=map(int,input().split())
#     ditu=[]
#     for j in range(0,n):
#         ditu.append([0]*m)
#     dfs(x,y,ditu,0)
#     print(num)





