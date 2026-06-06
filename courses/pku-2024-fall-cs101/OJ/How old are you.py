a=int(input())
while a!=1:
    if a%2==0:
        print(f'{a}/2={int(a/2)}')
        a=int(a/2)
    else:
        print(f'{a}*3+1={a*3+1}')
        a=a*3+1