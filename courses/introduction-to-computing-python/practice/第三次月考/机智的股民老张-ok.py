gupiao=list(map(int,input().split()))
n=len(gupiao)
out=[10001,0]
for i in range(0,n):
    if gupiao[i]<out[0]:
        out[0]=gupiao[i]
        continue
    out[1]=max(out[1],gupiao[i]-out[0])
print(out[-1])