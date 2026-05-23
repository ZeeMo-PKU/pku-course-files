def f(M,N):
    if N==1:
        return 1
    dp=[]
    for i in range(0,N+1):
        dp.append([1]*(M+1))
    for x in range(2,N+1):
        for y in range(1,M+1):
            if x>y:
                dp[x][y]=dp[y][y]
            else:
                dp[x][y]=dp[x-1][y]+dp[x][y-x]
    return dp[-1][-1]
t=int(input())
for i in range(0,t):
    M,N=map(int,input().split())
    print(f(M,N))