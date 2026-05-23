a=int(input())
b=list(map(int,input().split()))
c=[i for i in range(1,a+1)]
d=[]
for j in b:
    if j<=a:
        c.remove(j)
    else:
        d.append(j)
c.sort()
d.sort()
print(*c,sep=' ',end='\n')
print(*d,sep=' ',end='\n')