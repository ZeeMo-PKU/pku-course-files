l,m=map(int,input().split())
qujian=[]
for i in range(0,m):
    qujian.append(tuple(map(int,input().split())))
qujian.sort()
# print(qujian)
ans=0
zuo=qujian[0][0]
you=qujian[0][1]
for i in range(0,m):
    x1,x2=qujian[i]
    if x1<=you+1:
        you=max(you,x2)
    else:
        ans+=you-zuo+1
        # print(ans)
        zuo=x1
        you=x2
ans+=you-zuo+1
print(l+1-ans)