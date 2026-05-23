def king_number(points:list,n):
    points.sort(key=lambda x:(x[0],x[1]),reverse=True)

    y_max=float('-inf')
    x_now=float('-inf')
    number=0
    for x,y in points:
        if x==x_now:
            continue
        else:
            x_now=x
            if y>y_max:
                number+=1
                y_max=y
    return number

while True:
    n=int(input())
    if n==0:
        break
    else:
        points=[]
        for u in range(0,n):
            x,y=map(int,input().split())
            points.append((x,y))

        print(king_number(points,n))
