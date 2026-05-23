while True:
    try:
        a=input()
        a1=a.count('@')
        if a1==0 or a1>1 or a[0]=="@" or a[0]=='.' or a[-1]=='@' or a[-1]=='.' or '@.' in a or '.@' in a:
            print('NO')
        else:
            b=a[a.find('@'):]
            if not '.' in b:
                print('NO')
            else:
                print('YES')
    except EOFError:
        break