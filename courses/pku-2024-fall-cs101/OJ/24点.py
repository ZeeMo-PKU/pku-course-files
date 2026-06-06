a=int(input())
for i in range(0,a):
    a,b,c,d=map(int,input().split())
    if a+b+c+d==24 or a+b+c-d==24 or a+b-c+d==24 or a-b+c+d==24 or -a+b+c+d==24 or -a-b+c+d==24 or -a+b-c+d==24 or -a+b+c-d==24 or a-b-c+d==24 or a+b-c-d==24 or a+c-b-d==24 or -a-b-c+d==24 or -a-b+c-d==24 or -a+b-c-d==24 or a-b-c-d==24 or -a-b-c-d==24:
        print('YES')
    else:
        print('NO')