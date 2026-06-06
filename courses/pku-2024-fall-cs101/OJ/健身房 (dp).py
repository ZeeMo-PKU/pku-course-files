#dp
T,n=map(int,input().split())
tasks=[0]
for i in range(0,n):
    t,w=map(int,input().split())
    tasks.append((t,w))

f=[[0]+[-1]*T]
for i in range(0,n):
    f.append([0]+[-1]*T)
#print(f)
for i in range(1,n+1):
    for j in range(1,T+1):
        if j-tasks[i][0]>=0 and f[i-1][j-tasks[i][0]]>=0:
            f[i][j]=max(f[i-1][j-tasks[i][0]]+tasks[i][1],f[i-1][j])
        elif f[i-1][j]>0:
            f[i][j]=f[i-1][j]
print(f[-1][-1])
###############
T,n=map(int,input().split())
tasks=[]
for i in range(0,n):
    t,w=map(int,input().split())
    tasks.append((t,w))
f=[0]+[-float('inf')]*T
for (t,w) in tasks:
    for j in range(T,t-1,-1):
        f[j]=max(f[j],f[j-t]+w)
if f[-1]==-float('inf'):
    print(-1)
else:
    print(f[-1])

