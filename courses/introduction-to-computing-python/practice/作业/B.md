# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：leecode上的原题



代码：
gupiao=list(map(int,input().split()))
n=len(gupiao)
out=[10001,0]
for i in range(0,n):
    if gupiao[i]<out[0]:
        out[0]=gupiao[i]
        continue
    out[1]=max(out[1],gupiao[i]-out[0])
print(out[-1])
```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-7.png)




### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：
群里看到用同学用的递归，我也写了一个三个变量的函数


代码：
n,guo=map(int,input().split())
list_jipai=list(map(int,input().split()))
list_jipai.sort()

def f(list_jipai,n,guo):
    if guo==1:
        return sum(list_jipai)
    time_max_jipai=list_jipai.pop(-1)

    if time_max_jipai>sum(list_jipai)/(guo-1):
        return f(list_jipai,n-1,guo-1)

    else:
        return (sum(list_jipai)+time_max_jipai)/guo

print(f"{f(list_jipai,n,guo):.3f}")
```python

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-8.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：普通的遍历超时了



代码：
a = list(map(int, input().split(',')))
dp1 = [0] * len(a);
dp2 = [0] * len(a)
dp1[0] = a[0];
dp2[0] = a[0]
for i in range(1, len(a)):
    dp1[i] = max(dp1[i - 1] + a[i], a[i])
    dp2[i] = max(dp1[i - 1], dp2[i - 1] + a[i], a[i])
print(max(dp2))
```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-9.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：
太难了放弃了


代码：
result = float("inf")
n, m = map(int, input().split())
store_prices = [input().split() for _ in range(n)]
you= [input().split() for _ in range(m)]
la=[0]*m
def dfs(i,sum1):
    global result
    if i==n:
        jian=0
        for i2 in range(m):
            store_j=0
            for k in you[i2]:
                a,b=map(int,k.split('-'))
                if la[i2]>=a:
                    store_j=max(store_j,b)
            jian+=store_j
        result=min(result,sum1-(sum1//300)*50-jian)
        return
    for i1 in store_prices[i]:
        idx,p=map(int,i1.split(':'))
        la[idx-1]+=p
        dfs(i+1,sum1+p)
        la[idx-1]-=p
dfs(0,0)
print(result)
```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-11.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：
开始用的bfs，记录岛1所有的点，再记录岛2所有的点，超时了


代码：
import collections
def main():
    n=int(input())
    #grid=[[0]*(n+2)]
    grid=[]
    for i in range(n):
        p=list(int(x) for x in input())
        #p.insert(0,0)
        #p.append(0)
        grid.append(p)
    grid.append([0]*(n+2))
    visited = [[False for _ in range(n)] for _ in range(n)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    sr, sc = -1, -1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                sr, sc = r, c
                break
    q = collections.deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1 and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    for r in range(n):
        for c in range(n):
            if visited[r][c] == True and grid[r][c] == 1:
                q.append((r, c))
    step = 0
    while q:
        curLen = len(q)
        for _ in range(curLen):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    if grid[nr][nc] == 1:
                        return step
                    q.append((nr, nc))
        step += 1
    return step
print(main())
```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-12.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：
考试的时候理解错题意了，第二个样例数据一直过不去


代码：
n=int(input())
a0,b0=map(int,input().split())
numbers=[]
for _ in range(n):
    a,b=map(int,input().split())
    numbers.append((a,b))
numbers.sort(key=lambda x:(x[0]*x[1]))
result=0
for i in range(n):
    result=max(result,a0//numbers[i][1])
    a0*=numbers[i][0]
print(result)
```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-13.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
这次月考，只AC1，太难了，要放弃计概一段时间了，这段时间主要学习英语，然后写一下期末的论文，等几天在继续学习计概吧。




