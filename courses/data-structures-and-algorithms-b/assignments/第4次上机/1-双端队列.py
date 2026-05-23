from collections import deque
n=int(input())
for i in range(0,n):
    m=int(input())
    A=deque()
    for j in range(0,m):
        type,x=map(int,input().split())
        if type==1:
            A.append(x)
        else:
            if x==0:
                A.popleft()
            elif x==1:
                A.pop()
    if A:
        print(*A)
    else:
        print('NULL')