q=input()
a=list(map(int,input().split()))
e=0
d=0
for i in a:
    e+=i
    if e<0 and i<0:
        d+=1
        e=0
print(d)
