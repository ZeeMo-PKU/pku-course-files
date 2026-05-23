qianshu=int(input())
mianes=[1,5,10,20,50,100]
dp=[float("inf")]*(qianshu+1)
dp[0]=0
for miane in mianes:
    for i in range(miane,qianshu+1):
        if i-miane>=0:
            dp[i]=min(dp[i-miane]+1,dp[i])
print(dp[-1])