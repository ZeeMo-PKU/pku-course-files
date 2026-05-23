n=int(input())
numbers=list(map(int,input().split()))
dp=[0]*n
dp[0]=numbers[0]
for i in range(1,n):
    for j in range(0,i):
        if numbers[j]<numbers[i]:
            dp[i]=max(dp[i],dp[j]+numbers[i])
    if dp[i]==0:
        dp[i]=numbers[i]
print(max(dp))
