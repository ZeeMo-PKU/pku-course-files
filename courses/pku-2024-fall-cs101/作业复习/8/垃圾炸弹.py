d=int(input())
n=int(input())
rubbishs=[]
for j in range(0,n):
    x,y,i=map(int,input().split())
    rubbishs.append((x,y,i))
points=[]
for ax in range(0,1025):
    for ay in range(0,1025):
        uuu=0
        for (x,y,i) in rubbishs:
            if abs(x-ax)<=d and abs(y-ay)<=d:
                uuu+=i
        points.append(uuu)
boom=max(points)
print(points.count(boom),boom)
################
#AI give this
d = int(input())
n = int(input())
rubbishs = []
for _ in range(n):
    x, y, i = map(int, input().split())
    rubbishs.append((x, y, i))

# 初始化一个 1025x1025 的网格
grid = [[0] * 1025 for _ in range(1025)]

# 预处理每个垃圾点的影响范围
for x, y, i in rubbishs:
    for dx in range(-d, d + 1):
        for dy in range(-d, d + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 1025 and 0 <= ny < 1025:
                grid[nx][ny] += i

# 找到最大值及其出现次数
max_value = max(max(row) for row in grid)
count_max = sum(row.count(max_value) for row in grid)

print(count_max, max_value)