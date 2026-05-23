N,B=map(int,input().split())
list_jiage=[0]+list(map(int,input().split()))
list_tiji=[0]+list(map(int,input().split()))
f=[[0]*(B+1)]
for i in range(0,N):
    f.append([0]*(B+1))
for i in range(1,N+1):
    for j in range(B,0,-1):
        if j-list_tiji[i]>=0:
            f[i][j]=max(f[i-1][j],f[i-1][j-list_tiji[i]]+list_jiage[i])
print(f[-1][-1])
