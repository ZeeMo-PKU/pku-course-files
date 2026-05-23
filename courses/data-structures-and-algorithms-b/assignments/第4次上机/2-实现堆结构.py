import heapq

t = int(input())
for i in range(0, t):
    n = int(input())
    A = []
    for j in range(0, n):
        a = input()
        if a[0] == '2':
            q = heapq.heappop(A)
            print(q)
        else:
            u = int(a[2:])
            heapq.heappush(A, u)