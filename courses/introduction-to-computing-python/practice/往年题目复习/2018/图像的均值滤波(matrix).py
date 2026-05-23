m,n=map(int,input().split())

tuxiang=[[0]*(n+2)]
for i in range(0,m):
    tuxiang.append([0]+list(map(int,input().split()))+[0])

tuxiang.append([0]*(n+2))
fangxiang={(0,0),(1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)}
for x in range(1,m):
    ans=[]
    for y in range(1,n):
        uu=0
        for dx,dy in fangxiang:
            uu+=tuxiang[x+dx][y+dy]
        if {x,y} in ()
        uu=int(uu/a)
        ans.append(uu)
    print(*ans)

