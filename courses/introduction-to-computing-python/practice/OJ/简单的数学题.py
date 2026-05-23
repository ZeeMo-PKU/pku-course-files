a=int(input())
for i in range(0,a):
    q=int(input())
    n=0
    sum1=(1+q)*q/2
    while q>=1:
        q=q//2
        n+=1
    sum2=-(1-2**n)
    print(int(sum1-2*sum2))