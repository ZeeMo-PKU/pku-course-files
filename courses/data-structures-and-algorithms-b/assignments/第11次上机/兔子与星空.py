class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        #为了让索引正好对应，相当于产生了一个字典

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
    nodes = set([node for edge in G for node in edge[:2]])
    uf = UnionFind(len(nodes))

    # 按权值升序，遍历 G 中的每一条边（u, v）
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            # 将 (u, v) 加入 T
            T.append((u, v, weight))
            # 在并查集中将 u, v 合并
            uf.union(u, v)

    return T

n=int(input())
zuobiao={}
for i in range(1,n+1):
