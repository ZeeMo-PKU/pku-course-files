#dp解答
n=int(input())
things=[]
for i in range(0,n):
    a1,a2=map(int,input().split())
    things.append((a1,a2))
#things.sort(key=lambda x:x[1])
f=[0]*(1+max(a2 for (a1,a2) in things))
for i in range(0,len(f)):
    for thing in things:
        if thing[1]<=i and thing[0]>0:
            f[i]=max(f[thing[0]-1]+1,f[i])
        if thing[1]<=i and thing[0]==0:
            f[i]=max(f[i],1)
print(max(f))
#greedy解答
n=int(input())
things=[]
for i in range(0,n):
    a1,a2=map(int,input().split())
    things.append((a1,a2))
things.sort(key=lambda x:x[1])
end=-1
out=0
for thing in things:
    if thing[0]>end:
        end=thing[1]
        out+=1
print(out)