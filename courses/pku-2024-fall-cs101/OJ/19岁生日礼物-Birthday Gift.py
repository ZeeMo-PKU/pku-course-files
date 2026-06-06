n=int(input())
for i in range(0,n):
    a=input()
    if '19' in a:
        print('Yes')
        continue
    else:
        a=int(a)
        if a%19==0:
            print('Yes')
        else:
            print('No')
