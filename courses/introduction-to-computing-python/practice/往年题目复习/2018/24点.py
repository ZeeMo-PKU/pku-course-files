
def nengbuneng(x1,x2,x3,x4):
    X1=(x1,-x1)
    X2=(x2,-x2)
    X3=(x3,-x3)
    X4=(x4,-x4)

    for a1 in X1:
        for a2 in X2:
            for a3 in X3:
                for a4 in X4:
                    if a1+a2+a3+a4==24:
                        return 1

    return 0

m=int(input())
for i in range(m):
    x1,x2,x3,x4=map(int,input().split())
    if nengbuneng(x1,x2,x3,x4)==1:
        print('YES')
    else:
        print('NO')
