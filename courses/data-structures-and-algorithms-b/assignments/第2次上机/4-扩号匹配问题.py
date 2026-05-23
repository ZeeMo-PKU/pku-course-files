def main(juzi:str):
    l=len(juzi)
    you=[]
    zuo=[]
    zhan=[]
    for i in range(0,l):
        if juzi[i]=='(':
            zhan.append(i)
        if juzi[i]==')':
            if zhan:
                zhan.pop()
            else:
                you.append(i)
    if zhan:
        for j in zhan:
            zuo.append(j)

    ans=[' ']*l
    for k1 in zuo:
        ans[k1]='$'
    for k2 in you:
        ans[k2]='?'

    for q in ans:
        print(q,end='')
    print()


while True:
    try:
        juzi=input()
        print(juzi)
        main(juzi)
    except EOFError:
        break