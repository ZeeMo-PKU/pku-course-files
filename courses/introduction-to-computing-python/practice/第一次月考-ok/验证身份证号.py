a=int(input())
for i in range(0,a):
    b=input()
    sum_=int(b[0])*7+int(b[1])*9+int(b[2])*10+int(b[3])*5+int(b[4])*8+int(b[5])*4+int(b[6])*2+int(b[7])*1+int(b[8])*6+int(b[9])*3+int(b[10])*7+int(b[11])*9+int(b[12])*10+int(b[13])*5+int(b[14])*8+int(b[15])*4+int(b[16])*2
    k=sum_%11
    if k==0 and b[-1]=='1':
        print('YES')
    elif k==1 and b[-1]=='0':
        print('YES')
    elif k==2 and b[-1]=='X':
        print('YES')
    elif k==3 and b[-1]=='9':
        print('YES')
    elif k == 4 and b[-1] == '8':
        print('YES')
    elif k==5 and b[-1]=='7':
        print('YES')
    elif k==6 and b[-1]=='6':
        print('YES')
    elif k==7 and b[-1]=='5':
        print('YES')
    elif k==8 and b[-1]=='4':
        print('YES')
    elif k==9 and b[-1]=='3':
        print('YES')
    elif k==10 and b[-1]=='2':
        print('YES')
    else:
        print('NO')