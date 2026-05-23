class UnionFind:
    def __init__(self):
        self.parent={}

    def find(self,x):
        if x not in self.parent:
            self.parent[x]=x
            return x
        else:
            if self.parent[x]==x:
                return x
            else:
                return self.find(self.parent[x])

    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        self.parent[root_x]=root_y


def f(my_list):
    guanxi=UnionFind()
    for sentence in my_list:
        if '==' in sentence:
            guanxi.union(sentence[0],sentence[-1])
    for sentence in my_list:
        if '!=' in sentence:
            if guanxi.find(sentence[0])==guanxi.find(sentence[-1]):
                return False
    return True


n=int(input())
sentences=[]
for i in range(0,n):
    sentence=input()
    sentences.append(sentence)
print(f(sentences))