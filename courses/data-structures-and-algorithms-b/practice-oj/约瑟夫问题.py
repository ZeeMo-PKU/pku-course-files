from collections import deque

def f(n,m):
    shuzi=[i for i in range(1,n+1)]
    A=deque(shuzi)
    for i in range(0,n-1):
        A.rotate(-m+1)

        A.popleft()

    return A[0]

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    else:
        print(f(n,m))