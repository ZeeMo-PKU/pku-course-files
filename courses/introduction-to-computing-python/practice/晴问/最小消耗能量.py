#import math
def g(n,hs):
    if n==1:
        return hs[0]
    f=[0]+[0]*n
    for i in range(2,n+1):
        f[i]=min(f[i-1]+abs(hs[i]-hs[i-1]),f[i-2]+abs(hs[i]-hs[i-2]))
    return f[-1]
n=int(input())
hs=[float('inf')]+list(map(int,input().split()))
print(g(n,hs))