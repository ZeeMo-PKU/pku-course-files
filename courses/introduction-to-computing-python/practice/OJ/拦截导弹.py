from bisect import bisect_right
def intercept(heights):
    heights.reverse()
    dp=[]
    for height in heights:
        pos=bisect_right(dp,height)
        if pos< len(dp):
            dp[pos]=height
        else:
            dp.append(height)
    return len(dp)
k=int(input())
heights=list(map(int,input().split()))
print(intercept(heights))