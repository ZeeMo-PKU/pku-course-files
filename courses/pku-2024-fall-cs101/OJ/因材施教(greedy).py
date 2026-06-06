# n,m=map(int,input().split())
# a=list(input().split())
# a=[int(i) for i in a]
# a.sort()
# b=[]
# for j in range(0,len(a)-1):
#     b.append(a[j+1]-a[j])
# b.sort()
# out=0
# for op in range(0,n-m):
#     out+=b[op]
# print(out)


n,m=map(int,input().split())
a=list(input().split())
a=[int(i) for i in a]
huamingce={}
for i in range(1,n+1):
    huamingce[i]=a[i-1]

a.sort()
b=[]
for j in range(0,len(a)-1):
    b.append(a[j+1]-a[j])
b.sort()
out=0
for op in range(0,n-m):
    out+=b[op]
print(out)