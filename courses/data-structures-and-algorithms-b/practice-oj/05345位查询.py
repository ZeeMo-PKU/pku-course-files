n,m=map(int,input().split())
nums=list(map(int,input().split()))
while True:
    try:
        a,b=input().split()
        b=int(b)
        #C
        if a=="C":
            nums=[(n+b)%65535 for n in nums]
        #Q
        elif a=="Q":
            num_1=[str(bin(n>>b)) for n in nums]
            out=0
            for k in num_1:
                if k[-1]=='1':
                    out+=1
            print(out)
    except EOFError:
        break


