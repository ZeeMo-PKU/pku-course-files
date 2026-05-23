a=input()
if a[-1]=='C':
    a=float(a[0:-1])
    print(f'{round(a*1.8+32,2)}F')
elif a[-1]=='F':
    a=float(a[0:-1])
    b=(a-32)/1.8
    b=round(b,2)
    print(f'{b}C')