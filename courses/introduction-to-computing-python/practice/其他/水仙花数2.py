a0,b0=map(int,input().split())
k=[]
for i in range(a0,b0+1):
    a1=i//100
    a2=i//10
    a2=a2%10
    a3=i%10
    if i==a1**3+a2**3+a3**3:
        k.append(str(i))
print(' '.join(k))