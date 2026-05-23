# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：按照提示很好写



代码：
a,b=0,0
def dfs(a,b):
    global k
    dade,xiaode=max(a,b),min(a,b)

    beishu=dade//xiaode

    if beishu>1 or dade==xiaode:
        k=not k
        return
    else:
        k=not k
        dfs(dade-xiaode,xiaode)


while True:


    a,b=map(int,input().split())
    if {a,b}=={0}:
        break
    k=False
    dfs(a,b)
    if k:
        print('win')
    else:
        print('lose')


```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![img.png](img.png)




### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：既然学过双指针，那么我可以用一个四指针，但是终止条件有点难搞



代码：
n=int(input())
cengshu=-((-n)//2)
ceng=[0]*(cengshu+1)
juzhen=[]
for i in range(0,n):
    juzhen.append(list(map(int,input().split())))
shang,zuo,xia,you=0,0,n-1,n-1
k=0
while shang<xia:
    k+=1
    ooo=0
    for i in range(zuo,you+1):
        ooo+=juzhen[shang][i]
        ooo+=juzhen[xia][i]
    for j in range(shang+1,xia):
        ooo+=juzhen[j][zuo]
        ooo+=juzhen[j][you]
    ceng[k]=ooo
    shang+=1
    xia-=1
    zuo+=1
    you-=1
if shang==xia:
    ceng[-1]=juzhen[shang][shang]
# print(ceng)
print(max(ceng))
```python

```



代码运行截图 ==（至少包含有"Accepted"）==

![img_1.png](img_1.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：题目提示了用贪心，目前没想出来dp咋做



代码：
import heapq

n=int(input())
hede=list(map(int,input().split()))

health=0
num=0
fude=[]

for i in range(0,n):
    health+=hede[i]
    num+=1

    if hede[i]<0:
        heapq.heappush(fude,hede[i])

        if health<0:
            a=heapq.heappop(fude)
            num-=1
            health-=a
print(num)
```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![img_2.png](img_2.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：
合理利用辅助栈，但是要注意，栈顶元素要保持和最小的猪一致


代码：

```python
zhu=[]
zuiqingdezhu=[]
while True:
    try:
        a=input()

        if a[1]=='u':
            q,b=a.split()
            b=int(b)
            zhu.append(b)
            if not zuiqingdezhu or b<=zuiqingdezhu[-1]:
                zuiqingdezhu.append(b)

        elif a[1]=='o' and zhu:
            uuu=zhu.pop(-1)
            if uuu==zuiqingdezhu[-1]:
                zuiqingdezhu.pop(-1)

        elif a[1]=='i' and zuiqingdezhu:
            print(zuiqingdezhu[-1])

    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![img_3.png](img_3.png)




### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：已放弃本题，抓住简单题



代码：

```python
# m,n,p=map(int,input())
# #矩阵为m*n
# ditu=[]
# for i in range(0,m):
#     ditu.append(list(map(str,input().split())))
# ceshishuju=[]
# for i in range(0,p):
#     x1,y1,x2,y2=map(int,input().split())
#     ceshishuju.append((x1,y1,x2,y2))
# def dfs(x1,y1,x2,y2):
#
# 胡睿诚	174ms

import heapq
m, n, p = map(int, input().split())
info = []
for _ in range(m):
    info.append(list(input().split()))
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dijkstra(start_r, start_c, end_r, end_c):
    pos = []
    dist = [[float('inf')] * n for _ in range(m)]
    if info[start_r][start_c] == '#':
        return 'NO'
    dist[start_r][start_c] = 0
    heapq.heappush(pos, (0, start_r, start_c))
    while pos:
        d, r, c = heapq.heappop(pos)
        if r == end_r and c == end_c:
            return d
        h = int(info[r][c])
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and info[nr][nc] != '#':
                if dist[nr][nc] > d + abs(int(info[nr][nc]) - h):
                    dist[nr][nc] = d + abs(int(info[nr][nc]) - h)
                    heapq.heappush(pos, (dist[nr][nc], nr, nc))
    return 'NO'


for _ in range(p):
    x, y, z, w = map(int, input().split())
    print(dijkstra(x, y,z,w))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![img_4.png](img_4.png)




### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：
已放弃本题，着重简单题


代码：

```python
# fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
#
# def dfs(x,y,time):
#     global k
#     global min_time
#     time+=1
#     if ditu[x][y]=='E':
#         min_time==
#     if k*(time//k)==time:
#         for dx,dy in fangxiang:
#             if 0<=x+dx<c and 0<=y+dy<r:
#
#
#
#
# T=int(input())
# for i in range(0,T):
#     r,c,k=map(int,input().split())
#     ditu=[]
#     for j in range(0,r):
#         ditu.append(list(input()))
#     for a1 in range(0,r):
#         for a2 in range(0,c):
#             if ditu[a1][a2]=='S':
#                 qidian=(a1,a2)
#             elif ditu[a1][a2]=='E':
#                 zhongdian=(a1,a2)
import heapq
from math import inf

# 四个基本方向：右、下、左、上
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_shortest_path(grid, start, end, dimensions, cycle_length):
    """
    寻找从起点到终点的最短路径。

    :param grid: 地图信息（0为空地，1为石头）
    :param start: 起点坐标 (x, y)
    :param end: 终点坐标 (x, y)
    :param dimensions: 地图尺寸 (rows, cols)
    :param cycle_length: 穿过石头的时间周期
    :return: 最短时间或 "Oop!" 表示无法到达
    """
    rows, cols = dimensions
    visited = [[[False] * cols for _ in range(rows)] for _ in range(cycle_length)]
    priority_queue = [(0,) + start]  # 初始时间为0加上起点坐标

    while priority_queue:
        time, x, y = heapq.heappop(priority_queue)
        if (x, y) == end:  # 到达终点
            return time

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            new_time = time + 1

            if not (0 <= nx < rows and 0 <= ny < cols):  # 检查是否在地图内
                continue

            if grid[nx][ny] == 1 and new_time % cycle_length == 0 and not visited[new_time % cycle_length][nx][
                ny]:  # 穿石头
                visited[new_time % cycle_length][nx][ny] = True
                heapq.heappush(priority_queue, (new_time, nx, ny))
            elif grid[nx][ny] == 0 and not visited[new_time % cycle_length][nx][ny]:  # 普通空地
                visited[new_time % cycle_length][nx][ny] = True
                heapq.heappush(priority_queue, (new_time, nx, ny))

    return "Oop!"


def main():
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        rows, cols, cycle_length = map(int, input().split())
        grid = []
        start = None
        end = None

        for i in range(rows):
            line = input()
            row = []
            for j, char in enumerate(line):
                if char == "S":
                    start = (i, j)
                    row.append(0)  # 起点当空地
                elif char == "E":
                    end = (i, j)
                    row.append(0)  # 终点当空地
                elif char == "#":
                    row.append(1)  # 石头
                else:
                    row.append(0)  # 空地
            grid.append(row)

        result = find_shortest_path(grid, start, end, (rows, cols), cycle_length)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![img_6.png](img_6.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
这次作业前四个题都是自己写的，变换的迷宫已放弃，走山路还要再想一想，正在自学迪杰斯特拉算法，
不知道这个算法在机考中会不会考察（因为应该是数算的内容吧）
目前正在复习，不再学习很多新的算法
但是作业也让我学会了怎么用堆，有点收获




