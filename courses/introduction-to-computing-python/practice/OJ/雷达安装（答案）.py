import math

def solve(n, d, islands):
    if d < 0:
        return -1

    ranges = []
    for x, y in islands:
        if y > d:
            return -1
        delta = math.sqrt(d * d - y * y)
        ranges.append((x - delta, x + delta))

    if not ranges:
        return -1

    ranges.sort(key=lambda x:x[1])

    number = 1
    r = ranges[0][1]
    for start, end in ranges[1:]:
        if r < start:
            r = end
            number += 1

    return number

case_number = 0
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    case_number += 1
    islands = []
    for _ in range(n):
        islands.append(tuple(map(int, input().split())))

    result = solve(n, d, islands)
    print(f"Case {case_number}: {result}")
    input()