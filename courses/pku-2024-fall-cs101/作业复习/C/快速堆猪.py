zhu=[]
zuiqingdezhu=[]
while True:
    try:
        a=input()

        if a[1]=='u':
            q,b=a.split()
            b=int(b)
            zhu.append(b)
            if not zuiqingdezhu or b<=zuiqingdezhu[-1]:
                zuiqingdezhu.append(b)

        elif a[1]=='o' and zhu:
            uuu=zhu.pop(-1)
            if uuu==zuiqingdezhu[-1]:
                zuiqingdezhu.pop(-1)

        elif a[1]=='i' and zuiqingdezhu:
            print(zuiqingdezhu[-1])

    except EOFError:
        break