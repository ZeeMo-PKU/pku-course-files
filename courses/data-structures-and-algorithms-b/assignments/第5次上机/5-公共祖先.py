def zuxian(x):
    return x // 2


def g(a, b):
    a_zuxian = [a]
    while a > 0:
        a_zuxian.append(zuxian(a))
        a = zuxian(a)
    a_zuxian.reverse()
    l_a_zuxian = len(a_zuxian)
    b_zuxian = [b]
    while b > 0:
        b_zuxian.append(zuxian(b))
        b = zuxian(b)
    b_zuxian.reverse()
    l_b_zuxian = len(b_zuxian)
    for i in range(1, 999999):
        if i < l_b_zuxian and i < l_a_zuxian and a_zuxian[i] == b_zuxian[i]:
            continue
        else:
            return a_zuxian[i - 1]


def f(points, n):
    while n >= 2:
        x1 = points.pop()
        x2 = points.pop()
        points.append(g(x1, x2))
        n -= 1
    return points[0]


t = int(input())
for i in range(0, t):
    n = int(input())
    points = list(map(int, input().split()))
    print(f(points, n))
