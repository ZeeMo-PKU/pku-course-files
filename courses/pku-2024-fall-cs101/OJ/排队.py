
N,D=map(int,input().split())
a=[]
b=[]
for i in range(0,N):
    q=int(input())
    a.append(q)
    b.append(q)
for j in range(0,N-1):
    t=min(a)
    for u in range(0,N):
        if a[u]==t:
            break
        elif a[u]-t<=D:
            b[u]=t
            a[u]=99999999999
            break
    print(b)
for i1 in b:
    print(i1)