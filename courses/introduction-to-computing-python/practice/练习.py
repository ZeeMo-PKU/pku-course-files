n=int(input())
liwu=list(map(int,input().split()))
liwu2=[520-i for i in liwu]
qianzhuihe=[0]
for i in range(0,n):
    qianzhuihe.append(qianzhuihe[i]+liwu2[i])
#print(qianzhuihe)
ans=0
for i in range(0,n):
    for j in range(0,i):
        if qianzhuihe[i]-qianzhuihe[j]==0:
            ans=max(ans,i-j)
print(ans*520)