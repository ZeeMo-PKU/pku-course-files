from collections import deque

n,m=map(int,input().split())
rudu=[0]*(n+1)
shiwu=dict()
lujing=[0]*(n+1)
chudu=[0]*(n+1)
ans=0
for i in range(1,n+1):
    shiwu[i]=[]
for i in range(0,m):
    a,b=map(int,input().split())
    shiwu[b].append(a)
    rudu[a]+=1
    chudu[b]+=1

jilu=set()
for anm in range(1,n+1):
    if rudu[anm]==0 and chudu[anm]==0:
        jilu.add(anm)
A=deque([])
for i in range(1,n+1):
    if rudu[i]==0:
        lujing[i]=1
        A.append(i)
while A:
    a=A.popleft()
    for b in shiwu[a]:
        lujing[b]+=lujing[a]
        rudu[b]-=1
        if rudu[b]==0:
            A.append(b)
    if chudu[a]==0 and a not in jilu:
        ans+=lujing[a]
print(ans)

