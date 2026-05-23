from collections import deque
def f(chushi):
    ans=[]
    n=len(chushi)
    Q1=deque()
    Q2=deque()
    Q3=deque()
    Q4=deque()
    Q5=deque()
    Q6=deque()
    Q7=deque()
    Q8=deque()
    Q9=deque()
    QA=deque()
    QB=deque()
    QC=deque()
    QD=deque()
    shunxv=[Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9]
    for puke in chushi:
        shuzi=int(puke[-1])
        shunxv[shuzi-1].append(puke)
    for i in range(1,10):
        print(f'Queue{i}:{" ".join(shunxv[i-1])}')
    diyicipaixv=[]
    for biao in shunxv:
        while biao:
            puke=biao.popleft()
            diyicipaixv.append(puke)
    for puke in diyicipaixv:
        zimu=puke[0]
        if zimu=='A':
            QA.append(puke)
        elif zimu=='B':
            QB.append(puke)
        elif zimu=='C':
            QC.append(puke)
        else:
            QD.append(puke)
    print(f'QueueA:{" ".join(QA)}')
    print(f'QueueB:{" ".join(QB)}')
    print(f'QueueC:{" ".join(QC)}')
    print(f'QueueD:{" ".join(QD)}')
    while QA:
        ans.append(QA.popleft())
    while QB:
        ans.append(QB.popleft())
    while QC:
        ans.append(QC.popleft())
    while QD:
        ans.append(QD.popleft())
    print(*ans)

n=int(input())
pukes=list(input().split())
f(pukes)