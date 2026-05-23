n = int(input())
A = list(map(int, input().split()))
A.reverse()
A=[0]+A
dp = []
for i in range(0, n):
    dp.append([0, -1])
dp=[[0,0]]+dp
for i in range(1,n+1):
    for j in range(0,i):
        if A[i]>=dp[j][1] and dp[j][0]+1>dp[i][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = A[i]
        elif A[i]<dp[j][1] and dp[j][0]>=dp[i][0]:
            dp[i]=dp[j]
print(dp[-1][0])