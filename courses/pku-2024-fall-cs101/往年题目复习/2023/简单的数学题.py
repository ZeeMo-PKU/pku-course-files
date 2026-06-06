
t=int(input())
for i in range(0,t):
    n=int(input())
    out=((1+n)*n)//2
    # print(out)
    k=0
    while True:
        if 2**k<=n:
            k+=1
            continue
        k-=1
        break
    out-=2*((2**(k+1))-1)
    print(out)