#greedy
n=int(input())
trees = [(0,0)]
for i in range(0, n):
    x, h = map(int, input().split())
    trees.append((x, h))
if n<=2:
    print(n)

else:
    out=2
    ooo=0
    for i in range(2,n):
        if trees[i][0]-trees[i-1][0]>trees[i-1][1]*ooo+trees[i][1]:
            ooo=0
            out+=1
        elif trees[i][1]<trees[i+1][0]-trees[i][0]:
            ooo=1
            out+=1
        else:
            ooo=0
    print(out)
#答案
#差不多的
n = int(input())
s = [[int(x) for x in input().split()] for i in range(n)]
count = 2
if n == 1:
    print(1)
else:
    for i in range(1, n - 1):
        if s[i][0] - s[i - 1][0] > s[i][1]:
            count += 1
        elif s[i + 1][0] - s[i][0] > s[i][1]:
            count += 1
            s[i][0] += s[i][1]


    print(count)