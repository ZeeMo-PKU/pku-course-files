a,b=map(int,input().split())
c=list(map(int,input().split()))
n=0
for i in c:
    if i>b:
        n+=2
    else:
        n+=1
print(n)