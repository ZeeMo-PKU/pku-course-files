n=int(input())
h=[0]+list(map(int,input().split()))
f=[1]+[1]*n
for i in range(2,n+1):
    #f[i]=f[i-1]
    for j in range(1,i):
        if h[i]>h[j]:
            f[i]=max(f[j]+1,f[i])
print(max(f))#你不知道最后一个导弹有没有拦截