a,b,c=map(int,input().split())
s=a*((1+c)*c/2)
u=s-b
if u<=0:
    print(0)
else:
    print(int(u))