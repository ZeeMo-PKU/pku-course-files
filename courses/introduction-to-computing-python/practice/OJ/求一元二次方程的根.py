n=int(input())
for i in range(0,n):
    a,b,c=map(float,input().split())
    if b*b-4*a*c==0.00000:
        x1x2=-b/(2*a)
        x1x2=f'{float(x1x2):.5f}'
        print(f'x1=x2={x1x2}')
    elif b**2-4*a*c>0:
        x1=max((-b+(b*b-4*a*c)**0.5)/(2*a),(-b-(b*b-4*a*c)**0.5)/(2*a))
        x2=min((-b+(b*b-4*a*c)**0.5)/(2*a),(-b-(b*b-4*a*c)**0.5)/(2*a))
        x1=f'{float(x1):.5f}'
        x2=f'{float(x2):.5f}'
        if x1=='-0.00000':
            x1='0.00000'
        if x2=='-0.00000':
            x2='0.00000'
        print(f'x1={x1};x2={x2}')
    elif b**2-4*a*c<0:
        shibu=-b/(2*a)
        shibu=f'{float(shibu):.5f}'
        if shibu=='-0.00000':
            shibu='0.00000'
        xvbu=((4*a*c-b**2)**0.5)/(2*a)
        xvbu=f'{float(xvbu):.5f}'
        if '-' in xvbu:
            xvbu=xvbu[1:]
        print(f'x1={shibu}+{xvbu}i;x2={shibu}-{xvbu}i')
