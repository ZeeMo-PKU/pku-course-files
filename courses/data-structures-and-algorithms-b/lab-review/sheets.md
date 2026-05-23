算24点（错序遍历）
```python
for i in range(0,len(my_list)):
    for j in range(0,len(my_list)):
        if i!=j:
            a=my_list[i]
            b=my_list[j]
            left=[]
            for z in range(0,len(my_list)):
                if z!=i and z!=j:
                    left.append(my_list[z])
            if make_24(left+[a+b]) or make_24([a-b]+left) or make_24([a*b]+left):
                return True
            if b!=0 and make_24([a/b]+left):
                return True
```
放苹果（递归算法）
```python
def count_ways(m, n):
    # 如果没有苹果，只有一种分法：每个盘子放0个
    if m == 0:
        return 1
    # 如果没有盘子但还有苹果，不可能分
    if n == 0:
        return 0
    
    # 总分法 = 当前盘子放0个苹果的情况 + 至少放1个苹果的情况
    return count_ways(m, n - 1) + count_ways(m - n, n)
```
链表（以约瑟夫问题为示例）
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    # 添加节点（尾插）
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # 指向自己构成环
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
    # 打印链表
    def print_list(self):
        if not self.head:
            return
        cur = self.head
        while True:
            print(cur.value, end=" -> ")
            cur = cur.next
            if cur == self.head:
                break
    # 约瑟夫问题模拟
    def josephus(self, m):
        if not self.head or self.head.next == self.head:
            return self.head.value

        prev = None
        cur = self.head

        while cur.next != cur:  # 只要还有多于一个人
            # 数 m-1 下（因为当前已经是第一个人）
            for _ in range(m - 1):
                prev = cur
                cur = cur.next
            # 删除当前节点
            print(f"Eliminated: {cur.value}")
            prev.next = cur.next
            cur = cur.next
        return cur.value
```
判断链表是否有环（快慢指针算法）
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    if head is None or head.next is None:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```
优化后的KMP
```python
def improved_make_next(pattern):
    Next = [None] * len(pattern)
    i, k = 0, -1
    Next[0] = -1
    while i < len(pattern) - 1:
        if i == 0:
            Next[i] = -1
        while k >= 0 and pattern[i] != pattern[k]:
            k = Next[k]
        k += 1
        i += 1
        if pattern[i] == pattern[k]:
            Next[i] = Next[k]
        else:
            Next[i] = k
    return Next

def kmp_search(text, pattern, next_array):
    i = j = 0  # i: text index, j: pattern index
    results = []

    while i < len(text):
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next_array[j]

        if j == len(pattern):
            results.append(i - j)  # 记录匹配位置
            j = next_array[j]  # 继续查找下一个匹配

    return results
```
字典的各种用法
```python
keys = my_dict.keys() #产生一个键列表
values = my_dict.values() #产生一个值列表
del my_dict['age']  #删除键值对，pop也可以
#遍历键、值、键值对
for key in my_dict：
for value in my_dict.values()：
for key, value in my_dict.items():
```
二叉树的实现
```python
class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
```
遍历二叉树（以中序为示例）
```python
def in_order(tree):
    if tree:
        in_order(tree.left_child)
        print(tree.key)
        in_order(tree.right_child)
```
二叉堆
```python
class MinHeap:
    def __init__(self):
        self.heap = []

    # 获取父节点索引
    def parent(self, i):
        return (i - 1) // 2

    # 获取左子节点索引
    def left(self, i):
        return 2 * i + 1

    # 获取右子节点索引
    def right(self, i):
        return 2 * i + 2

    # 插入元素
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    # 上浮操作（插入时使用）
    def _heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    # 删除并返回最小值
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # 把最后一个元素移到根节点
        self._heapify_down(0)           # 下沉操作维护堆性质
        return root

    # 下沉操作（删除/替换根节点时用）
    def _heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    # 查看当前堆顶（最小值）
    def get_min(self):
        return self.heap[0] if self.heap else None

    # 原地构建堆（从无序数组建堆）
    def build_min_heap(cls, arr):
        heap = cls()
        heap.heap = arr[:]
        for i in range(len(arr) // 2 - 1, -1, -1):
            heap._heapify_down(i)
        return heap
```
哈夫曼算法
```python
import heapq
# 定义哈夫曼树节点类
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char      # 字符（如果是叶子节点）
        self.freq = freq      # 频率
        self.left = None      # 左子节点
        self.right = None     # 右子节点

    # 用于优先队列比较
    def __lt__(self, other):
        return self.freq < other.freq
# 统计频率并构建哈夫曼树
def build_huffman_tree(text):
    if not text:
        return None

    # 统计字符频率
    frequency = Counter(text)

    # 创建优先队列（最小堆）
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # 合并节点，直到只剩一个根节点
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heapq.heappop(heap)
```
二分查找标准代码
```python
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # 防止溢出
        
        if arr[mid] == target:
            return mid  # 找到目标值，返回索引
        elif arr[mid] < target:
            left = mid + 1  # 目标值在右半部分
        else:
            right = mid - 1  # 目标值在左半部分
            
    return -1  # 没有找到目标值
```
并查集（标准代码）
```python
class UnionFind:
    def __init__(self, n):
        """
        初始化并查集。
        :param n: 节点数量
        """
        self.parent = list(range(n))  # 初始化每个节点的父节点为自身
        self.rank = [0] * n           # 初始化每个节点的秩（树的高度）

    def find(self, x):
        """
        查找节点x的根节点，并进行路径压缩。
        :param x: 节点索引
        :return: 根节点索引
        """
        if self.parent[x] != x:  # 如果当前节点不是根节点
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        """
        合并两个节点所在的集合。
        :param x: 第一个节点索引
        :param y: 第二个节点索引
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:  # 如果两个节点不在同一个集合
            if self.rank[root_x] < self.rank[root_y]:  # 按秩合并
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
```
例题：宗教信仰
```python
class UnionFind:
    def __init__(self):
        self.parent=dict()
        self.rank=dict()

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)


        if root_x != root_y:  # 如果两个节点不在同一个集合
            if self.rank[root_x] < self.rank[root_y]:  # 按秩合并
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

    def is_con(self,x,y):
        if self.find(x) != self.find(y):
            return False
        else:
            return True

case=1
while True:
    n,m=map(int,input().split())
    if n>0:
        A=UnionFind()
        for i in range(1,n+1):
            A.parent[i]=i
            A.rank[i]=1
        for i in range(0,m):
            stu1,stu2=map(int,input().split())
            A.union(stu1,stu2)
        ans=set()
        for i in range(1,n+1):
            q=A.find(i)
            if q not in ans:
                ans.add(q)
        print(f'Case {case}: {len(ans)}')
    else:
        break
    case+=1
```
```python
def find(parent, x):
    """ 查找 x 的根节点，并进行路径压缩 """
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 路径压缩
    return parent[x]

def union(parent, rank, x, y):
    """ 合并 x 和 y 所在的集合，按秩合并优化 """
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

case_number = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:  # 输入结束条件
        break
    
    # 初始化并查集
    parent = list(range(n + 1))  # 学生编号从 1 到 n，所以需要 n+1 的长度
    rank = [0] * (n + 1)  # 初始化秩为 0
    
    # 处理每对关系
    for _ in range(m):
        i, j = map(int, input().split())
        union(parent, rank, i, j)
    
    # 统计连通分量数量（即不同根节点的数量）
    religions = set()
    for i in range(1, n + 1):
        religions.add(find(parent, i))
    
    print(f"Case {case_number}: {len(religions)}")
    case_number += 1
```
DFS模板
```python
import sys
sys.setrecursionlimit(10000)
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()  # 初始化一个集合用于记录已访问节点
    visited.add(start)  # 将起始节点标记为已访问
    print(start)  # 可以在这里处理节点，比如打印节点值
    
    for next_node in graph[start]:  # 对于每个相邻的节点
        if next_node not in visited:  # 如果该节点尚未被访问
            dfs_recursive(graph, next_node, visited)  # 递归调用dfs函数
```
BFS模板
```python
from collections import deque

def bfs(graph, start):
    visited = set()  # 初始化一个集合用于记录已访问节点
    queue = deque([start])  # 使用队列来存储待访问的节点

    while queue:
        vertex = queue.popleft()  # 从队首取出元素
        if vertex not in visited:
            print(vertex)  # 处理节点
            visited.add(vertex)  # 标记为已访问
            # 添加所有未访问的邻居到队尾
            queue.extend(set(graph[vertex]) - visited)
```
可回溯的BFS模板
```python
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
```
最小生成树（Prim算法）
```python
import heapq

def prim(G):
    """
    G: 邻接表表示的图，格式为 {node: [(weight, neighbor), ...]}
    返回最小生成树的边集 T
    """
    # 初始化
    n = len(G)  # 节点数量
    T = []  # 最小生成树的边集
    Dist = [float('inf')] * n  # 初始距离列表，所有节点到当前MST的距离设为无穷大
    Pred = [-1] * n  # 前驱节点列表，记录每个节点在MST中的前驱节点
    visited = [False] * n  # 记录节点是否已加入MST
    
    # 任选一个顶点作为起点，这里选择0号节点
    start = 0
    Dist[start] = 0  # 起点到自身的距离为0
    heap = [(0, start)]  # 创建最小堆，插入起点，键值为Dist值
    
    while heap:
        dist, u = heapq.heappop(heap)
        
        if visited[u]:
            continue  # 如果节点已经访问过，则跳过
        
        visited[u] = True  # 标记节点u为已访问
        
        if Pred[u] != -1:  # 如果u不是起始节点，则将(u, Pred[u])加入T中
            T.append((u, Pred[u], dist))

        # 更新与u相邻的所有节点v的距离和前驱节点
        for weight, v in G[u]:
            if not visited[v] and weight < Dist[v]:
                Dist[v] = weight
                Pred[v] = u
                heapq.heappush(heap, (Dist[v], v))  # 将更新后的节点v重新加入堆中        
    return T
```
Kruskal算法
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
def kruskal(G):
    """
    G: 带权连通无向图，格式为 [(u, v, weight), ...]
    返回最小生成树的边集 T
    """
    # 初始化生成树边集 T
    T = []
    # 将 G 中的所有边按照权值升序排序
    edges = sorted(G, key=lambda x: x[2])
    # 创建并查集，G 中的每个结点自成一个集合
    uf = UnionFind(len(set([node for edge in G for node in edge[:2]])))
    
    # 按权值升序，遍历 G 中的每一条边 (u, v)
    for u, v, weight in edges:
        # 如果 u, v 在并查集中属于不同集合（不同连通分量）：
        if uf.find(u) != uf.find(v):
            # 将 (u, v) 加入 T
            T.append((u, v, weight))
            # 在并查集中将 u, v 合并
            uf.union(u, v)
    
    return T
```
Dijkstra 算法标准模板(通过回溯可以找到路径)
```python
import heapq

def dijkstra(graph, start):
    """
    使用 Dijkstra 算法计算起始点到图中所有其它点的最短路径。
    
    :param graph: 加权图，以邻接表形式表示。例如：{u: [(v, w), ...], ...}
                  其中 u 是起点，(v, w) 是终点和对应的权重。
    :param start: 起始顶点。
    :return: 返回两个字典，分别为到达每个节点的最短距离 dist 和前驱节点 prev。
    """
    dist = {vertex: float('inf') for vertex in graph}  # 初始化距离字典
    prev = {vertex: None for vertex in graph}          # 初始化前驱节点字典
    dist[start] = 0                                    # 起始点到自身的距离为0
    priority_queue = [(0, start)]                      # 最小堆，初始化为起始点
    
    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        
        # 如果当前距离大于记录的距离，则跳过
        if current_dist > dist[current_vertex]:
            continue
        
        # 遍历相邻节点
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            
            # 只有在找到更短路径时更新
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist, prev
```
floyd算法示例
```python
import sys
sys.setrecursionlimit(100000000)
# 弗洛伊德算法
def floyd():
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    parents[i][j] = parents[k][j]  # 更新父结点
# 打印路径
def print_path(i, j):
    if i != j:
        print_path(i, parents[i][j])
    print(j, end='-->')

# Data [u, v, cost]
datas = [
    [0, 1, 2],
    [0, 2, 6],
    [0, 3, 4],
    [1, 2, 3],
    [2, 0, 7],
    [2, 3, 1],
    [3, 0, 5],
    [3, 2, 12],
]

n = 4

# 无穷大
inf = 9999999999

# 构图
graph = [[(lambda x: 0 if x[0] == x[1] else inf)([i, j]) for j in range(n)] for i in range(n)]
parents = [[i] * n for i in range(4)]  # 关键地方，i-->j 的父结点初始化都为i
for u, v, c in datas:
    graph[u][v] = c	# 因为是有向图，边权只赋给graph[u][v]
    #graph[v][u] = c # 如果是无向图，要加上这条。
floyd()

print('Costs:')
for row in graph:
    for e in row:
        print('∞' if e == inf else e, end='\t')
    print()

print('\nPath:')
for i in range(n):
    for j in range(n):
        print('Path({}-->{}): '.format(i, j), end='')
        print_path(i, j)
        print(' cost:', graph[i][j])
```
拓扑排序算法示例
```python
from collections import defaultdict, deque

def topological_sort(graph):
    # 统计入度
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    # 将入度为0的节点加入队列
    queue = deque([node for node in graph if indegree[node] == 0])
    result = []
    # 拓扑排序
    while queue:
        node = queue.popleft()
        result.append(node)
        # 将该节点的邻接节点的入度减1，并将入度为0的节点加入队列
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # 如果结果中的节点数等于图中的节点数，则拓扑排序成功
    if len(result) == len(graph):
        return result
    else:
        return None
```
最大上升子序列
```python
def max_sum_increasing_subsequence(n, nums):
    dp = nums[:]  # 初始化为自身，即长度为1的子序列
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    
    return max(dp)
```
逆波兰算法【sf要求】（示例代码）
```python
def eval_rpn(tokens):#注意：这里放进去一个元素是字符串类型的list
    stack = []

    for token in tokens:
        if token not in "+-*/":
            # 将数字压入栈中
            stack.append(int(token))
        else:
            # 弹出两个操作数
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # 注意 Python 中 -1/2 是 -1，而不是像多数 RPN 解释器一样为 0
                stack.append(int(a / b))  # 向零取整
    # 最终结果在栈顶
    return stack[0]
```
滑动窗口（以找最大值为例）
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()  # 双端队列
        for i, x in enumerate(nums):
            # 1. 入
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 入队
            # 2. 出
            if i - q[0] >= k:  # 队首已经离开窗口了
                q.popleft()
            # 3. 记录答案
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])
        return ans
```
判断图是否是连通的
```python
#BFS思路
import sys
from collections import deque

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def is_connected_bfs(n, edges):
    # 构建邻接表表示的图
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 初始化访问数组
    visited = [False] * (n + 1)
    
    # 从第一个节点开始进行BFS
    bfs(graph, visited, 1)
    
    # 检查所有节点是否都被访问过
    return all(visited[i] for i in range(1, n + 1))

# 读取输入
input_data = sys.stdin.read().strip().split('\n')
lines = [line.split() for line in input_data]
n, m = map(int, lines[0])
edges = [tuple(map(int, line)) for line in lines[1:]]

# 判断图是否连通
if is_connected_bfs(n, edges):
    print("YES")
else:
    print("NO")

#DFS思路
import sys

def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def is_connected_dfs(n, edges):
    # 构建邻接表表示的图
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 初始化访问数组
    visited = [False] * (n + 1)
    
    # 从第一个节点开始进行DFS
    dfs(graph, visited, 1)
    
    # 检查所有节点是否都被访问过
    return all(visited[i] for i in range(1, n + 1))

# 读取输入
input_data = sys.stdin.read().strip().split('\n')
lines = [line.split() for line in input_data]
n, m = map(int, lines[0])
edges = [tuple(map(int, line)) for line in lines[1:]]

# 判断图是否连通
if is_connected_dfs(n, edges):
    print("YES")
else:
    print("NO")
```
前序+中序-->后序
```python
def build_tree(preorder, inorder):
    if not preorder:
        return ""
    
    root = preorder[0]
    root_index = inorder.index(root)

    left_in = inorder[:root_index]
    right_in = inorder[root_index+1:]

    left_size = len(left_in)
    left_pre = preorder[1:1+left_size]
    right_pre = preorder[1+left_size:]

    left_post = build_tree(left_pre, left_in)
    right_post = build_tree(right_pre, right_in)

    return left_post + right_post + root


# 多组输入处理
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        preorder, inorder = line.split()
        postorder = build_tree(preorder, inorder)
        print(postorder)
    except:
        break
```
一些细碎的小点
1：优化-前缀和
```python
    #1：提前算出来列表前面的和
    #2：@lru_cache
    #3:一些重复的东西提前算出来
        cubes = [i**3 for i in range(N+1)]
        cube_set = {v: i for i, v in enumerate(cubes)}  # 创建立方值到其根的映射
```
2:优化：优化为二分查找
3：优化（剪枝）：dfs提前剪枝
4：小数点保留问题
```python
    print(f'{a:.6f}')
```
5:质数-欧拉筛
```python
def Eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
```
6：join的使用
```python
print('  '.join(list_1))
```
7:math库中的一些用法
```python
math.ceil(x)	返回不小于 x 的最小整数（向上取整）
math.floor(x)	返回不大于 x 的最大整数（向下取整）
math.trunc(x)	截断小数部分，返回整数部分
math.fabs(x)	返回 x 的绝对值（浮点数）
math.gcd(a, b)	返回 a 和 b 的最大公约数
math.pow(x, y)	返回 x 的 y 次幂（x^y）
math.sqrt(x)	返回 x 的平方根
math.exp(x)	返回 e^x
math.log(x,base)	返回以 base 为底的对数（默认自然对数 ln）
```
8:枚举
``` python
for i,x in enumerate(list),遍历list中的（下标，值）对
```
9:递归爆栈：这个用以下代码解决
```python
from sys import setrecurisonlimit
setrecursionlimit(10000)#python 默认 200
```
10:在列表中找某一个元素的索引
```python
list.index(yuansu)
```
11:组合数计算
```python
#组合数计算
def C(m,n):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
```
12：将字符串映射为整数编号（可以解决一些问题）
13：列表题一般以索引入队列，而不是元素本身。
14:列表排序
```python
list.sort(key=lambda x:x[0])
```