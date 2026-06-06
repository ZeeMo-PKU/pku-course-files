n=10**4
prime=[True for _ in range(n+1)]
p=2
while p*p<=n:
    if prime[p]:
        for i in range(p*p,n+1,p):
            prime[i]=False
    p+=1
zhishu=set([p for p in range(2,n+1) if prime[p]])
mubiao=set(i**2 for i in zhishu)

n,m=map(int,input().split())
for i in range(0,n):
    fenshu=list(map(int,input().split()))
    ans=0
    for num in fenshu:
        if num in mubiao:
            ans+=num

    ans/=len(fenshu)
    if ans==0:
        print(0)
    else:
        print(f'{ans:.2f}')