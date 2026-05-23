from shutil import which

n,m=map(int,input().split())
tangguo=[]
for i in range(0,n):
    a,b=map(int,input().split())
    c=a/b
    tangguo.append((a,c,b))

tangguo.sort(key=lambda x:-x[1])
# print(tangguo)
out=0
for a,b,c in tangguo:
    # print(out)
    if m>c:
        m-=c
        out+=a
    elif m<c:
        out+=b*m
        break
print(f'{out:.1f}')