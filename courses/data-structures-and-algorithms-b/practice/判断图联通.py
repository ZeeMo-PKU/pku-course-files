from collections import deque


def bfs(ditu,qidian,n):
    A=deque([])
    A.append(qidian)
    seen=set()
    seen.add(qidian)
    while A:
        x=A.popleft()
        for y in ditu[x]:
            if y not in seen:
                A.append(y)
                seen.add(y)
    if len(seen)==n:
        return 'YES'
    else:
        return 'NO'


n,m=map(int,input().split())
ditu=dict()
for i in range(1,n+1):
    ditu[i]=[]
for i in range(0,m):
    a,b=map(int,input().split())
    ditu[a].append(b)
    ditu[b].append(a)
print(bfs(ditu,1,n))