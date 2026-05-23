from collections import deque
import copy
fangxiang={(0,1),(0,-1),(1,0),(-1,0)}

def bfs(x1,y1,x2,y2,ditu2):
    global bushu
    A=deque([(x1,y1,0)])
    while A:
        (ax,ay,c)=A.popleft()
        # print(ax,ay,c,x2,y2)
        for dx,dy in fangxiang:
            for u in range(1,77):
                if 0<=ax+dx*u<h+2 and 0<=ay+dy*u<w+2:
                    # print(ax+dx*u,ay+dy*u)
                    if ax+dx*u == x2 and ay+dy*u == y2:
                        return c+1
                    if ditu2[ax + dx * u][ay + dy * u] == ' ':
                        A.append((ax+dx*u,ay+dy*u,c+1))
                        ditu2[ax + dx * u][ay + dy * u]='X'
                    else:
                        break
                else:
                    break
    return -1


board=0
while True:
    board+=1
    w,h=map(int,input().split())
    #h*w的矩阵
    if {w,h}=={0}:
        break
    print(f'Board #{board}:')
    ditu=[[' ']*(w+2)]
    for i in range(0,h):
        ditu.append([' ']+list(input())+[' '])
    ditu.append([' ']*(w+2))
    # print(ditu)
    pair_num=0
    while True:
        pair_num+=1
        y1,x1,y2,x2=map(int,input().split())
        if {x1,x2,y1,y2}=={0}:
            break
        ditu2=copy.deepcopy(ditu)





        a=bfs(x1,y1,x2,y2,ditu2)
        if a==-1:
            print(f'Pair {pair_num}: impossible.')
        else:
            print(f'Pair {pair_num}: {a} segments.')
    print()
