def xiugai(ditu,n,m):

n,m=map(int,input().split())
ditu=[]
for i in range(0,n):
    ditu.append(list(map(int,input().split())))
out=xiugai(ditu,n,m)
for k in out:
    print(*k)