N,C=map(int,input().split())
points=[]
for i in range(0,N):
    points.append(int(input()))
dp=[[0]*(C+1)]
for i in range(0,N):
    dp.append([0]*(C+1))
    dp[i][j]=