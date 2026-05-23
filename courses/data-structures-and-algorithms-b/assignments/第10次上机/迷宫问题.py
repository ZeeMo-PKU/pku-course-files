from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(map,start,end):
    A=deque()
    shangyibu={start:None}
    seen={start}
    x1, y1 = start
    x2, y2 = end
    A.append((x1, y1))

    while A:
        x,y=A.popleft()
        current=(x,y)
        if (x,y) == end:
            current=(x,y)
            ans=[]
            while current:
                ans.append(current)
                current=shangyibu[current]
            ans.reverse()
            return ans
        else:
            for dx,dy in directions:
                new_x,new_y=x+dx, y+dy
                if map[new_x][new_y]!=1 and (new_x,new_y) not in seen:
                    A.append((new_x,new_y))
                    seen.add((new_x,new_y))
                    shangyibu[(new_x,new_y)]=current


maze=[]
maze.append([1]*7)
for i in range(0,5):
    maze.append([1]+list(map(int,input().split()))+[1])
maze.append([1]*7)
start = (1,1)
end = (5,5)
out=bfs(maze,start,end)
for x in out:
    a,b=x
    a-=1
    b-=1
    print((a,b))