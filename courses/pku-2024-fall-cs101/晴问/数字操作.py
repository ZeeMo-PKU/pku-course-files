#不需要队列呢？from collections import deque
def bfs(n):
    seen={1}
    step=0
    A=[1]
    while A:
        B=[]
        for i in A:
            if i+1==n or i*2==n:
                return step+1
            if i+1 not in seen:
                B.append(i+1)
                seen.add(i+1)
            if i*2<n and i*2 not in seen:
                B.append(i*2)
                seen.add(i*2)
        step+=1
        A=B[:]
n=int(input())

print(bfs(n))

