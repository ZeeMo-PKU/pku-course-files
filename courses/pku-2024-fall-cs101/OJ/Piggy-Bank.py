T=int(input())
for i in range(0,T):
    e,f=map(int,input().split())

    zhongliang_1=f-e+1

    n=int(input())
    huobi=[]
    for j in range(0,n):
        huobi.append(tuple(map(int,input().split())))
    huobi.sort(key=lambda x:x[1])
    zuiqing=huobi[0][1]

    dp=[float('inf')]*zhongliang_1
    dp[0]=0

    for k in range(zuiqing,zhongliang_1):
        for a1,a2 in huobi:
           if k-a2>=0:
               dp[k]=min(dp[k-a2]+a1,dp[k])
    if dp[-1]!=float('inf'):
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')
    else:
        print('This is impossible.')