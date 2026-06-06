n=int(input())
f=[0]+[0]*n
if n<=2:
    print(n)
else:
    f[1]=1
    f[2]=2
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
    print(f[-1])