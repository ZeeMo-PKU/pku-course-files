def f(n,list_1):
    if len(list_1)!=n:
        print("NO")
        return
    #可以先行判断
    if n>=3:
        for i in range(1,n-2):
            if list_1[i-1]>max(list_1[i],list_1[i-1]) and list_1[i+1]>list_1[i]:
               print('NO')
               return
    zhan=[]
    mubiao=0
    daan=[]
    for i in range(1,n+1):
        zhan.append(i)
        daan.append(f"PUSH {i}")
        while zhan and mubiao!=n:
            if zhan[-1]==list_1[mubiao]:
                daan.append(f'POP {zhan[-1]}')
                zhan.pop()
                mubiao+=1
            else:
                break
    if mubiao==n:
        for op in daan:
            print(op)
    # else:
    #     print("NO")
    #     return
n=int(input())
list_1=list(map(int,input().split()))
f(n,list_1)