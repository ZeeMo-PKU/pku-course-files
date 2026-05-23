n=int(input())
xvlie=list(map(int,input().split()))
dp=[0]*n
for i in range(0,n):
    dp[i]=xvlie[i]
    for j in range(0,i):
        if xvlie[i]>xvlie[j]:
            dp[i]=max(dp[i],dp[j]+xvlie[i])
print(max(dp))