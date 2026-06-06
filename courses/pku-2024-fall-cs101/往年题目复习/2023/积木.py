def chazhao(chushi,)
N=int(input())
jimu=[[1]]
for i in range(0,4):
    jimu.append(set(map(int,input().split())))
for j in range(N):
    A=list(map(int,input().split()))
    seen=[1]*5
    for i in A:
        for op in range(1,5):
            if seen[op]==1:
                continue

