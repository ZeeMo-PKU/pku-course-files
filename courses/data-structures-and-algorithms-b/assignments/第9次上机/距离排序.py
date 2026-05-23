import math
def length(a,b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
n=int(input())
zuobiao=list(map(int,input().split()))
points=[]
for i in range(0,n):
    x=zuobiao[3*i]
    y=zuobiao[3*i+1]
    z=zuobiao[3*i+2]
    points.append((x,y,z))
juli=[]
for i in range(0,n):
    for j in range(i+1,n):
        juli.append((points[i],points[j],length(points[i],points[j])))
juli.sort(key=lambda x:-x[-1])
for x in juli:
    point_1,point_2,len=x
    print(f'{point_1}-{point_2}={len:.2f}')