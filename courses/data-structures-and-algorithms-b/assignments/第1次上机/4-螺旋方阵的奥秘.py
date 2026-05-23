N,M=map(int,input().split())
ditu=[[-1]*(N+2)]
for i in range(0,N):
    ditu.append([-1]+[0]*N+[-1])
ditu.append([-1]*(N+2))
x=1#行
y=1#列
num=1

fangxiang=[(0,1),(1,0),(0,-1),(-1,0)]
zhizhen=0
while True:
    if num==M:
        print(x,y)
        break
    ditu[x][y]=-1
    dx=fangxiang[zhizhen][0]
    dy=fangxiang[zhizhen][1]
    if ditu[x+dx][y+dy]==0:
        num+=1
        x+=dx
        y+=dy
    else:
        zhizhen+=1
        zhizhen=zhizhen%4
        dx = fangxiang[zhizhen][0]
        dy = fangxiang[zhizhen][1]
        num += 1
        x += dx
        y += dy