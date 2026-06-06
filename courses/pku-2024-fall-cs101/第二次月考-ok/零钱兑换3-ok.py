#dp
n,m=map(int,input().split())
n=tuple(map(int,input().split()))
dp=[0]+[float('inf')]*m
for i in range(m+1):
    for j in n:
        if i-j<0:
            break
            #保证是大的4
        dp[i]=min(dp[i-j]+1,dp[i])
if dp[m]!='inf':
    print(dp[m])
else:
    print(-1)
