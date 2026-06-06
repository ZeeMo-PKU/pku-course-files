a=int(input())
for i in range(0,a):
    b=int(input())
    c=[0]*b
    for j in range(1,b+1):
        for k in range(1,b+1):
            if k%j==0:
                if c[k-1]==0:
                    c[k-1]=1
                else:
                    c[k-1]=0
    print(sum(c))

