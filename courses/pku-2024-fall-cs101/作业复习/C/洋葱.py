n=int(input())
cengshu=-((-n)//2)
ceng=[0]*(cengshu+1)
juzhen=[]
for i in range(0,n):
    juzhen.append(list(map(int,input().split())))
shang,zuo,xia,you=0,0,n-1,n-1
k=0
while shang<xia:
    k+=1
    ooo=0
    for i in range(zuo,you+1):
        ooo+=juzhen[shang][i]
        ooo+=juzhen[xia][i]
    for j in range(shang+1,xia):
        ooo+=juzhen[j][zuo]
        ooo+=juzhen[j][you]
    ceng[k]=ooo
    shang+=1
    xia-=1
    zuo+=1
    you-=1
if shang==xia:
    ceng[-1]=juzhen[shang][shang]
# print(ceng)
print(max(ceng))