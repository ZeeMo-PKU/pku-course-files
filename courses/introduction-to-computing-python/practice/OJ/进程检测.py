k=int(input())
for i in range(0,k):
    n=int(input())
    a=[]
    for j in range(0,n):
        a.append(tuple(map(int,input().split())))
    a.sort(key=lambda x: x[1])
    out=1
    point=a[0][1]
    for op in range(0,len(a)):
        if a[op][0]>point:
            out+=1
            point=a[op][1]
    print(out)