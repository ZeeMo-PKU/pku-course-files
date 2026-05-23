class MinHeap:
    #基本函数
    def __init__(self):
        self.list=[None]
        self.size=0
    def is_empty(self):
        if self.size==0:
            return True
        return False
    #添加元素
    def add(self,value):
        self.list.append(value)
        self.size+=1
        self._add_sort(value,self.size)
    #排序-上浮
    def _add_sort(self,value,position):
        now_node=value
        parent_node=self.list[position//2]
        while position>1:
            if parent_node>now_node:
                self.list[position],self.list[position//2]=self.list[position//2],self.list[position]
                position//=2
                parent_node=self.list[position//2]
            else:
                break

    #找最小
    def find_min(self):
        return self.list[1]
    #pop最小
    def heappop(self):
        answer=self.list[1]
        self.list[1]=self.list[self.size]
        self.list.pop()
        self.size -= 1
        self._pop_sort(1)
        return answer
    #排序-下沉
    def _pop_sort(self,position=None):
        if position is None:
            position=1
        while position * 2 <= self.size:  # 至少有一个子节点
            left_child = position * 2
            right_child = position * 2 + 1
            smaller_child = left_child  # 默认左子节点较小

            # 如果右子节点存在且更小
            if right_child <= self.size and self.list[right_child] < self.list[left_child]:
                smaller_child = right_child

            # 如果当前节点比子节点大，则交换
            if self.list[position] > self.list[smaller_child]:
                self.list[position], self.list[smaller_child] = self.list[smaller_child], self.list[position]
                position = smaller_child
            else:
                break

t=int(input())
for i in range(0,t):
    A=MinHeap()
    n=int(input())
    for j in range(0,n):
        a=input()
        if a[0]=='1':
            a,b=a.split()
            b=int(b)
            A.add(b)
        else:
            print(A.heappop())

