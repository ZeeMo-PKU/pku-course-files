#假设有一排石子，每堆石子有一个重量，
# 每次只能合并相邻的两堆石子。
# 合并的代价是这两堆石子的总重量。
# 目标是找到一种合并顺序，使得总的合并代价最小。
n=int(input())
shizi=[0]+list(map(int,input().split()))
sum_=[0]*(n+1)
#计算前缀和
for i in range(1,n+1):
    sum_[i]=sum_[i-1]+shizi[i]
#0-1背包
f=[]
for i in range(0,n+1):
    f.append([0]*(n+1))
#print(f)
for i in range(n,0,-1):
    for j in range(i+1,n+1):
        f[i][j]=float('inf')
        for k in range(0,j-i):
            f[i][j]=min(f[i][j],f[i][i+k]+f[i+k+1][j]+sum_[j]-sum_[i-1])
print(f[1][n])
#3
#3 1 2
#9