while True:
    n, d = map(int, input().split())
    if n==0:
        break
    points=[]
    for i in range(0,n):
        x,y=map(int,input().split())
        if y>d:
            print(-1)
            break
        points.append((x,y))
