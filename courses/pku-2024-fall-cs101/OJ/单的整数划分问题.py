dp=[0]*51
dp[1]=1
dp[2]=2
for i in range(3,51):
    dp[i]+=dp[i-1]

while True:
    try:
        n=int(input())
        print(dp[n])
    except EOFError:
        break