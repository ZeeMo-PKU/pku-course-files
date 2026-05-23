a=int(input())
for i in range(0,a):
    c=1
    d=1
    u=int(input())
    if u%2==0 and u>2:
        for j in range(1,u//2):
            c=c+d
            d=d+c
        print(max(c,d))
    elif u<3:
        print(1)
    else:
        for o in range(0,u//2):
            c=c+d
            d=d+c
        print(min(c,d))