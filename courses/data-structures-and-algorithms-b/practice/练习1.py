from collections import deque
fangxiang={(1,0),(-1,0),(0,1),(0,-1)}

def bfs(ditu,qidian,zhongdian):
    visited=set()
    A=deque([qidian])
    visited.add(qidian)
    parent={qidian:None}
    while A:
        x,y=A.popleft()
        if (x,y)==zhongdian:
            break


        for dx,dy in fangxiang:
            x1,y1=x+dx,y+dy
            if (x1,y1) not in visited and 0<=x1<5 and 0<=y1<5 and ditu[x1][y1]==0:
                A.append((x1,y1))
                visited.add((x1,y1))
                parent[x1,y1]=(x,y)

    ans = [(x, y)]
    while zhongdian:
        zhongdian = parent[zhongdian]
        ans.append(zhongdian)
    ans.reverse()
    return ans[1:]


ditu=[]
for i in range(5):
    ditu.append(list(map(int,input().split())))
qidian=(0,0)
zhongdian=(4,4)
Q=bfs(ditu,qidian,zhongdian)
for i in Q:
    print(i)