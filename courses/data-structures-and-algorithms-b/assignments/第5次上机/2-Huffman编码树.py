import heapq

def f(n,weights):
    WPL=0
    heapq.heapify(weights)
    while n>=2:
        n-=1
        left_child_node=heapq.heappop(weights)
        right_child_node=heapq.heappop(weights)
        parent_node=left_child_node+right_child_node
        heapq.heappush(weights,parent_node)
        WPL+=parent_node
    return WPL

t=int(input())
for i in range(0,t):
    n=int(input())
    weights=list(map(int,input().split()))
    print(f(n,weights))