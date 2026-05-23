n1=int(input())
for i in range(0,n1):
    n,m,b=map(int,input().split())
    jineng={}
    for j in range(0,n):
        ti,xi=map(int,input().split())
        if ti not in jineng:
            jineng[ti]=[xi]
        else:
            jineng[ti].append(xi)
    for _ in jineng.values():
        _.sort(reverse=True)
    for aaa in sorted(jineng):
        b-=sum(jineng[aaa][:m])
        if b<=0:
            time=aaa
            break
    if b>0:
        print('alive')
    else:
        print(time)