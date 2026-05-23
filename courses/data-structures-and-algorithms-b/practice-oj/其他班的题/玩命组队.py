from collections import deque

n,m=map(int,input().split())
dic=dict()
for i in range(1,n+1):
    dic[i]=[]
for i in range(n-1):
    a,b=map(int,input().split())
    dic[a].append(b)
A=deque([])
A.append(m)
ans=0
while A:
    x=A.popleft()
    ans+=1
    if x in dic:
        for y in dic[x]:
            A.append(y)
print(ans)