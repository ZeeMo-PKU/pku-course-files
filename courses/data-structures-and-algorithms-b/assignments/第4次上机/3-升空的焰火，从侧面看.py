from collections import deque

# 读取输入
N = int(input())
nodes = [None] * (N + 1)  # 节点数组，0号位置不使用

# 初始化节点
for i in range(1, N + 1):
    nodes[i] = {'val': i, 'left': None, 'right': None}

# 构建二叉树
for i in range(1, N + 1):
    left, right = map(int, input().split())
    if left != -1:
        nodes[i]['left'] = nodes[left]
    if right != -1:
        nodes[i]['right'] = nodes[right]

# 广度优先搜索（BFS）
root = nodes[1]  # 根节点
queue = deque([root])
result = []

while queue:
    level_size = len(queue)
    last_node = None

    for _ in range(level_size):
        node = queue.popleft()
        last_node = node['val']  # 记录当前层的最后一个节点

        # 将子节点加入队列
        if node['left']:
            queue.append(node['left'])
        if node['right']:
            queue.append(node['right'])

    result.append(last_node)  # 当前层的最后一个节点加入结果

# 输出结果
print(' '.join(map(str, result)))