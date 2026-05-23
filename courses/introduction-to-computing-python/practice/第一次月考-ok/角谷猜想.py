a=int(input())
while True:
    if a==1:
        print('End')
        break
    elif a%2==1 and a>1:
        print(f'{a}*3+1={a*3+1}')
        a = a * 3 + 1
    else:
        print(f'{a}/2={int(a/2)}')
        a=int(a/2)