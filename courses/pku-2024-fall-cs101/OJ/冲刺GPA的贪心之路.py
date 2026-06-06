h=int(input())
m=int(input())
al=[]
for i in range(0,m):
    a,b=map(int,input().split())
    al.append((a,a*b))
al.sort(reverse=True,key=lambda x:x[1])
h-=0.5*m
for j in al:
    if h<
