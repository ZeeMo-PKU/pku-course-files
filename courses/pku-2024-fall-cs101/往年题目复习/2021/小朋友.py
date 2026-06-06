n=int(input())
woban=[]
qitaban=[]
xiaohai=list(map(int,input().split()))
xiaohai.sort()
xiaohai=tuple(xiaohai)
for i in range(1,n+1):
    if i in xiaohai:
        continue
    else:
        woban.append(i)
for k in xiaohai:
    if k>n:
        qitaban.append(k)
print(*woban)
print(*qitaban)
