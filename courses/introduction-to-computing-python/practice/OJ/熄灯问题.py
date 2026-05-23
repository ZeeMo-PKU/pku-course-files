# biao=[]
# for i in range(0,5):
#     biao.append(list(map(int,input().split())))
# #5*6
#
# out=[[0]*6 for _ in range(5)]
#
# def bianhuan(x,y,biaozhi):
#     if biaozhi==1:
#         if out[x][y]==1:
#             out[x][y]=0
#         else:
#             out[x][y]=1
#     elif biaozhi==0:
#         if biao[x][y]==1:
#             biao[x][y]=0
#         else:
#             biao[x][y]=1
#     return
#
#
#
# chulibiao={(0,0),(0,1),(0,-1),(1,0),(-1,0)}
#
# def kaideng(x,y):
#     bianhuan(x,y,1)
#     for dx,dy in chulibiao:
#         nx=x+dx
#         ny=y+dy
#         if 0<=nx<5 and 0<=ny<6:
#             bianhuan(nx,ny,0)
#
#
#
#
# def chuliqiansihang():
#     for x in range(0,4):
#         for y in range(0,6):
#             if biao[x][y]==1:
#                 kaideng(x+1,y)
#
#
# chuliqiansihang()
# print(biao)
# print(out)
# while sum(biao[-1])>0:
#     for i in range(0,6):
#         if biao[-1][i]==1:
#             kaideng(0,i)
#     chuliqiansihang()
#
#
#第一行全组合
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n,a):
    
    if n==6:
        return diyihang
    if n==0:
        return []

    diyihang.append([1]+f(n-1))
    diyihang.append([0]+f(n-1))

f(6)
print(diyihang)
# #
# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def f(n):
#     if n == 0:
#         return ((),)  # 返回一个包含空元组的单元素元组
#
#     result = []
#     for seq in f(n - 1):
#         result.append((1,) + seq)  # 创建新元组并添加到结果列表
#         result.append((-1,) + seq)  # 创建新元组并添加到结果列表
#
#     return tuple(result)  # 将结果列表转换为元组以便缓存
#
#
# # 调用函数并收集结果
# combinations = list(f(6))
#
# # 打印结果
# for combination in combinations:
#     print(list(combination))  # 如果需要以列表形式打印
#
# # 如果你需要将结果存储在一个列表中，可以这样做
# diyihang = [list(combination) for combination in combinations]


