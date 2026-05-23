#dp题目
def cutcut(n,a,b,c):
    dp=[-100]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        for i2 in (a,b,c):
            if i>=i2 and dp[i-i2]!=-100:#(这里可以判断一下):
                dp[i]=max(dp[i],dp[i-i2]+1)
    return dp[n]
n,a,b,c=map(int,input().split())
print(cutcut(n,a,b,c))
import?