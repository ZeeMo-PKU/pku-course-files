a=input()
biao=[]
for j in a:
    if j=='R':
        biao.append(1)
    else:
        biao.append(0)
n=len(biao)
cishu=0

ooo=0
if biao[0]==0:
    for i in range(0,n):
        if biao[i]==0:
            ooo+=1
            i+=1
        else:
            break
else:
    i=0
if ooo!=0:
    cishu+=1
while i<n:
    if biao[i]==0:
        i+=1
        k=1
        while i<n and biao[i]==0:
            k+=1
            i+=1
        if k==1:
            cishu+=1
        else:
            cishu+=2
    else:
        i+=1
        continue
print(cishu)
