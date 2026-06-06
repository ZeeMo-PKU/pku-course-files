N,B=map(int,input().split())
w=[0]+list(map(int,input().split()))
v=[0]+list(map(int,input().split()))
f=[]
for i in range(0,N+1):
    f.append([0]*(B+1))

for i in range(1,N+1):
    for j in range(1,B+1):
        if j-v[i]>=0:
            f[i][j]=max(f[i-1][j],f[i-1][j-v[i]]+w[i])
print(f[-1][-1])
#print(f)
#注意倒序遍历背包容量
N,B=map(int,input().split())
w=[0]+list(map(int,input().split()))
v=[0]+list(map(int,input().split()))
f=[0]*(B+1)
for i in range(1,N+1):
    for j in range(B,v[i]-1,-1):
        if j-v[i]>=0:
            f[j]=max(f[j],f[j-v[i]]+w[i])
print(f[-1])
#########
n,b=map(int, input().split())
price=[0]+[int(i) for i in input().split()]
weight=[0]+[int(i) for i in input().split()]
bag=[[0]*(b+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if weight[i]<=j:
            bag[i][j]=max(price[i]+bag[i-1][j-weight[i]], bag[i-1][j])
        else:
            bag[i][j]=bag[i-1][j]
print(bag[-1][-1])

