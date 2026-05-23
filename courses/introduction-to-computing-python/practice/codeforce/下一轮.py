a,b=input().split()
e=0
b=int(b)
c=list(map(int,input().split()))
for i in c:
    if i>=c[b-1] and i>0:
        e+=1
print(e)