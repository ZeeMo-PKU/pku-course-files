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