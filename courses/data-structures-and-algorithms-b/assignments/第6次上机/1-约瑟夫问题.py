#约瑟夫问题
class Node:
    def __init__(self,key,pre=None,last=None):
        self.key=key
        self.pre=pre
        self.last=last
    def delete(self):
        self.pre.last=self.last
        self.last.pre=self.pre
        return self.last
def f(n,m):
    head=Node(1)
    now_node=head
    for i in range(2,n+1):
        new_node=Node(i)
        new_node.pre=now_node
        now_node.last=new_node
        now_node=new_node
    now_node.last=head
    head.pre=now_node

    now_node=head
    while n>1:
        for i in range(0,m-1):
            now_node=now_node.last
        now_node=now_node.delete()
        n-=1
    return now_node.key



while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    else:
        print(f(n,m))

