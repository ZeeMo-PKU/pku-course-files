class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.rank=[0]*n

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x!=root_y:
            self.parent[root_x]=root_y

    def same(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        return root_x==root_y

n,m=map(int,input().split())
A=UnionFind(n)
for i in range(0,m):
    a,b=map(int,input().split())
    A.union(a,b)
ans=set()
for i in range(1,n+1):
    ans.add(A.find(i))
print(len(ans))
