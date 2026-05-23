a=input()
if ord(a[0])<60:
    a=int(a)
    a1=a//1000
    print('M'*a1,end='')
    a2=(a//100)%10
    if a2==4:
        print('CD',end='')
    elif a2==9:
        print('CM',end='')
    elif a2<=3:
        print('C'*a2,end='')
    elif 4<a2<9:
        print('D', end='')
        print('C'*(a2-5),end='')
    a3=(a//10)%10
    if a3 == 4:
        print('XL', end='')
    elif a3 == 9:
        print('XC', end='')
    elif a3 <= 3:
        print('X' * a3,end='')
    elif 4 < a3 < 9:
        print('L', end='')
        print('X' * (a3- 5), end='')
    a4=a%10
    if a4== 4:
        print('IV', end='')
    elif a4== 9:
        print('IX', end='')
    elif a4<= 3:
        print('I' * a4, end='')
    elif 4 < a4< 9:
        print('V', end='')
        print('I' * (a4- 5), end='')
else:
    year=0
    k=list(a)
    for i in k:
        if i=='I':
            year+=1
        if i == 'V':
            year +=5
        if i == 'X':
            year +=10
        if i == 'L':
            year +=50
        if i == 'C':
            year +=100
        if i == 'D':
            year +=500
        if i == 'M':
            year +=1000
    if 'IV'in a:
        year-=2
    if 'IX' in a:
        year -=2
    if 'XL'in a:
        year-=20
    if 'XC'in a:
        year-=20
    if 'CD'in a:
        year-=200
    if 'CM'in a:
        year-=200
    print(year)