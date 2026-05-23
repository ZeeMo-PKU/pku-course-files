from collections import deque

n,k=map(int,input().split())
A=deque()
A.append((n,0))
visited=set()
visited.add(n)
while A:
    (position,step)=A.popleft()
    visited.add(position)
    if position==k:
        print(step)
        break
    else:
        if position+1 not in visited and 0 <= position+1 <= 100000:
            A.append((position+1,step+1))
        if position-1 not in visited and 0 <= position-1 <= 100000:
            A.append((position-1,step+1))
        if position*2 not in visited and 0 <= position*2 <= 100000:
            A.append((position*2,step+1))

        continue