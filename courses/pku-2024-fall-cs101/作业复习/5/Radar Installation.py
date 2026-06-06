import math
uuu=0
while True:
    uuu+=1
    n,r=map(int,input().split())
    if {n,r}=={0}:
        break
    points=[]
    for i in range(0,n):
        x,y=map(int,input().split())
        points.append((x,y))
    if max(point[1] for point in points)>r:
        print(f'Case {uuu}: -1')
        input()
        continue
    ranges=[]
    for point in points:
        d=math.sqrt(r**2-point[1]**2)
        ranges.append((point[0]-d,point[0]+d))
    ranges.sort(key=lambda o:o[1])
    out=0
    youbianjie=float('-inf')
    for (a1,a2) in ranges:
        if a1>youbianjie:
            out+=1
            youbianjie=a2
    print(f'Case {uuu}: {out}')
    input()



