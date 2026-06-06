n,m=map(int,input().split())
jvzhen=[]
for i in range(0,n):
    jvzhen.append(list(map(int,input().split())))
for j in jvzhen:
    print(*j)