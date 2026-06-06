n,m=map(int,input().split())
ditu1=[[1]*(m+2)]
for i in range(0,n):
    ditu1.append([1]+list(map(int,input().split()))+[1])
ditu1.append([1]*(m+2))
ditu2=[[0]*(m+2)]
for i in range(0,n):
    ditu2.append([0]+list(map(int,input().split()))+[0])
ditu2.append([0]*(m+2))

quan=float('-inf')
fangxiang={(1,0),(-1,0),(0,1),(0,-1)}
def dfs(x,y,quan_now):
    global quan
    if x==n and y==m:
        quan=max(quan,quan_now+ditu2[n][m])
        return
    if ditu1[x][y]==0:
        quan_new=quan_now+ditu2[x][y]
        ditu1[x][y]=1
        for (dx,dy) in fangxiang:
            dfs(x+dx,y+dy,quan_new)
        ditu1[x][y]=0
dfs(1,1,0)
print(quan)
