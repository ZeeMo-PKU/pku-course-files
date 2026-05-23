while True:
    a,c,b=map(int,input().split())
    u=b-1+c-1
    kk=[]
    if a*b*c==0:
        break
    else:
        l=[i for i in range(1,a+1)]
        while len(l)>1:
            kk.append(l.pop(u))
            u=(u+b-1)%len(l)
        kk=kk+l
        print(*kk,sep=',')