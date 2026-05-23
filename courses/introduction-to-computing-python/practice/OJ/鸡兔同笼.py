foot=int(input())
if foot%2!=0:
    print('ERROR!')
else:
    b=foot//2
    if foot%4==0:
        a=foot//4
    else:
        a=foot//4+1
    print(f'{a} {b}')
