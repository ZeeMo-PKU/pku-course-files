while True:
    try:
        a=input()
        n=len(a)
        A=list(a)
        A.sort()
        out=True
        for i in range(1,n+1):
            b=list(str(int(a)*i)).sort()
            print(b,A)
            if b != A:
                out=False
                break
        print(out)
    except EOFError:
        break
