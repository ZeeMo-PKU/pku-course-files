m,n=map(int,input().split())
#m*n的一个矩阵
ditu=[[2]*(n+2)]
for i in range(0,m):
    ditu.append([2]+list(map(int,input().split()))+[2])
ditu.append([2]*(n+2))
ans=False
step_min=float('inf')
fangxiang={(-1,0),(1,0),(0,1),(0,-1)}
def dfs(x,y,step_now):
    global ans
    global step_min
    if ditu[x][y]==1:
        step_min=min(step_min,step_now)
        ans=True
        return
    if ditu[x][y]==0:
        step_new=step_now+1
        ditu[x][y]=2
        for (dx,dy) in fangxiang:
            dfs(x+dx,y+dy,step_new)
        ditu[x][y]=0
dfs(1,1,0)
if ans:
    print(step_min)
else:
    print('NO')