a,b=map(int,input().split())
c=list(map(int,input().split()))
n=0
for i in range(0,len(c)-1):
    if int(c[i])>=int(c[i+1]):
        if c[i]==c[i+1]:
            n+=1
            c[i+1]=c[i+1]+b
        else:
            n+=((int(c[i])-int(c[i+1]))//b+1)
            c[i+1]=c[i+1]+((int(c[i])-int(c[i+1]))//b+1)*b
print(n)