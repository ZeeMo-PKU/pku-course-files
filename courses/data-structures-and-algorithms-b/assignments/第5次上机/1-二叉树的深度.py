from collections import deque

n = int(input())
duiying = {}
for i in range(1, n + 1):
    a, b = map(int, input().split())
    duiying[i] = (a, b)
sousuo = deque([(1, 1)])
while sousuo:
    (point, depth) = sousuo.popleft()
    if duiying[point][0] > 0:
        sousuo.append((duiying[point][0], depth + 1))
    if duiying[point][1] > 0:
        sousuo.append((duiying[point][1], depth + 1))
print(depth)
