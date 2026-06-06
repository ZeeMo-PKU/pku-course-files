import heapq

n=int(input())
hede=list(map(int,input().split()))

health=0
num=0
fude=[]

for i in range(0,n):
    health+=hede[i]
    num+=1

    if hede[i]<0:
        heapq.heappush(fude,hede[i])

        if health<0:
            a=heapq.heappop(fude)
            num-=1
            health-=a
print(num)