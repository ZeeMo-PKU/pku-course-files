def oo(n):
    if n<=2:
        return n
    f=[1,1]+[0]*(n-1)
    for i in range(2,n+1):
        f[i]=(f[i-1]+f[i-2])%10007
    return f[-1]
n=int(input())
print(oo(n))