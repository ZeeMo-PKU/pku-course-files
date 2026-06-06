a=int(input())
for i in range(0,a):
    b=input()
    c=int(b[0:2])
    y=int(b[2:4])
    m=int(b[4:6])
    if m==1:
        m=13
        y=y-1
        if y==-1:
            y=99
            c-=1
    if m==2:
        m=14
        y=y-1
        if y==-1:
            y=99
            c-=1
    d=int(b[6:8])
    w=(y+y//4+c//4-2*c+(26+26*m)//10+d-1)%7
    wed={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    print(wed[w])