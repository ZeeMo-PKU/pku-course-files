while True:
    a,b=map(int,input().split())
    u=b-1#因为可恶的索引从0开始
    if a==0 and b==0:
        break
    else:
        l=[i for i in range(1,a+1)]
        while len(l)>1:
            del(l[u])
            u=(u+b-1)%len(l)
        print(*l)