a=eval(input())
for i in range(0,a):
    b=input()
    if len(b)<=10:
        print(b)
    else:
        d1=b[0]
        d2=len(b)-2
        d3=b[-1]
        print(f'{d1}{d2}{d3}')