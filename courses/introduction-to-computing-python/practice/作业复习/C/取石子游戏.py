a,b=0,0
def dfs(a,b):
    global k
    dade,xiaode=max(a,b),min(a,b)

    beishu=dade//xiaode

    if beishu>1 or dade==xiaode:
        k=not k
        return
    else:
        k=not k
        dfs(dade-xiaode,xiaode)


while True:


    a,b=map(int,input().split())
    if {a,b}=={0}:
        break
    k=False
    dfs(a,b)
    if k:
        print('win')
    else:
        print('lose')

