#dfs
n,m=map(int,input().split())
ditu=[[float('-inf')]*(m+2)]
for i in range(0,n):
    ditu.append([float('-inf')]+list(map(int,input().split()))+[float('-inf')])
ditu.append([float('-inf')]*(m+2))


quan=float('-inf')
quan_new=0
fangxiang={(0,1),(0,-1),(1,0),(-1,0)}



def dfs(x,y,quan_now):
    global quan
    if x == n and y == m:
        quan = max(quan, quan_now+ditu[n][m])
        return
    if ditu[x][y]!=float('-inf'):
        quan_new=quan_now+ditu[x][y]
        guisu=ditu[x][y]
        ditu[x][y]=float('-inf')
        for (dx,dy) in fangxiang:
            dfs(x+dx,y+dy,quan_new)
        ditu[x][y]=guisu
dfs(1,1,0)
print(quan)
#print(ditu)