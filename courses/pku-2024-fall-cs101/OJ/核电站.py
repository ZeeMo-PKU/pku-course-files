N,M=map(int,input().split())
f=[1]+[0]*N
for i in range(1,N+1):
    if M>i:
        f[i]=2**i
    else:
        for j in range(1,M+1):
            f[i]+=f[i-j]
print(f[-1])
