n = int(input())
m = 2 * n - 1

array = [[None] * m for i in range(m)]

# 从1计数
current_x = 1
current_y = 1
count, total_count = 1, m * m

while count <= total_count:
    if count == 1:
        current_x, current_y = 1, n
    elif current_x == 1 and current_y == m:
        current_x += 1
    elif current_x == 1:
        current_x = m
        current_y += 1
    elif current_y == m:
        current_y = 1
        current_x -= 1
    elif array[current_x - 2][current_y]:
        current_x += 1
    else:
        current_x -= 1
        current_y += 1
    array[current_x - 1][current_y - 1] = count
    count += 1

for x in array:
    print(" ".join([str(i) for i in x]))