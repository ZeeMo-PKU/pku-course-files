import heapq
class PriorityQueue:
    def __init__(self):
        self.list=[]
        self.index=0
        self.size=0
    def add(self,item,priority):
        heapq.heappush(self.list,(priority,self.index,item))
        self.index+=1
        self.size+=1
    def popmin(self):
        answer=heapq.heappop(self.list)[-1]
        self.size-=1
        return answer

