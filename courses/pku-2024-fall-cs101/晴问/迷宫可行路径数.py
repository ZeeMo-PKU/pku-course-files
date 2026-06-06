#保护圈
fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
count=0
def dfs(x,y,ditu):
    global count
    for (x_,y_) in fangxiang:
        if x+x_==n and y+y_==n:
            count+=1
            continue
        elif ditu[x+x_][y+y_]==0:
            ditu[x][y]=1
            dfs(x+x_,y+y_,ditu)
            ditu[x][y]=0



n,m=map(int,input().split())
ditu=[[1]*(m+2)]
for i in range(0,n):
    ditu.append([1]+list(map(int,input().split()))+[1])
ditu.append([1]*(m+2))
dfs(1,1,ditu)
print(count)