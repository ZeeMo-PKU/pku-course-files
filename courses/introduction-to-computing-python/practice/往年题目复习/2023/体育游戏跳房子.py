from linecache import cache
from collections import deque

out=[]

def bfs(chushi,jieshu):
    bushu=0
    seen={chushi}
    b=[]
    A=deque([(chushi,'',0)])
    while A:
        x,b,d=A.popleft()
        if x==jieshu:
            print(d)
            out.append(b)
            while A:
                x,b,k=A.popleft()
                if x==jieshu and k==d:
                    out.append(b[:])
            return bushu
        if x*3 not in seen:
            A.append((x*3,b+'H',d+1))
            seen.add(x*3)
        if x // 2 not in seen:
            A.append((x//2,b+'O',d+1))
            seen.add(x//2)
while True:
        a,b=map(int,input().split())
        if a==0 and b==0:
            break
        out=[]
        bfs(a,b)
        out.sort()
        print(out[0])









