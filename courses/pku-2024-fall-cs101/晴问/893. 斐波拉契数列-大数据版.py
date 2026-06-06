#import sys
#sys.setrecursionlimit(1000000000000000000+9)
n=int(input())
if n<3:
    print(1)

else:
    mod=1e9+7
    a,b=1,1

    for i in range(1,n):
        c=int((a+b)%mod)
        a,b=b,c
    print(a)