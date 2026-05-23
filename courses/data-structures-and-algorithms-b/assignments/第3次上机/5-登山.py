def g(list_1):

    l=len(list_1)
    dp=[1]*l
    for i in range(0, l):
        for j in range(0, i):
            if list_1[i] > list_1[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]
def f(n,haiba):
    answer=[]
    if n==2:
        return 2 if haiba[0]!=haiba[-1] else 1
    for i in range(1,n):
        shangsheng=g(list(haiba[:i+1]))
        uu=haiba[i:]
        uu.reverse()
        xiajiang=g(uu)
        answer.append(shangsheng+xiajiang-1)
    return max(answer)
n=int(input())
haiba=list(map(int,input().split()))
print(f(n,haiba))