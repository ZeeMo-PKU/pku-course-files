n,m,k=map(int,input().split())
ditu=[[1]*(m+2)]
for i in range(0,n):
    ditu.append([1]+list(map(int,input().split()))+[1])
ditu.append([1]*(m+2))
fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
daan=0
def dfs(x,y,step):
    global daan
    global k
    if step>=k:
        return
    for (x1,y1) in fangxiang:
        if x+x1==n and y+y1==m and step==k-1:
            daan+=1
        if ditu[x+x1][y+y1]==0:
            ditu[x][y]=1
            dfs(x+x1,y+y1,step+1)
            ditu[x][y]=0
dfs(1,1,0)
if daan:
    print('Yes')
else:
    print('No')