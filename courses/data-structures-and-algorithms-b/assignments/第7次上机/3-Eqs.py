a1,a2,a3,a4,a5=map(int,input().split())
sancifang={i:i**3 for i in range(-50,51)}
ans=dict()
values = [i for i in range(-50, 51) if i != 0]
p=0
for x1 in values:
    if x1!=0:
        for x2 in values:
            if x2!=0:
                out=a1*sancifang[x1]+a2*sancifang[x2]
                if out not in ans:
                    ans[out]=1
                else:
                    ans[out]+=1
for x3 in values:
    if x3!=0:
        for x4 in values:
            if x4 != 0:
                for x5 in values:
                    if x5 != 0:
                        k=a3*sancifang[x3]+a4*sancifang[x4]+a5*sancifang[x5]
                        k=0-k
                        if k in ans:
                            p+=ans[k]
print(p)