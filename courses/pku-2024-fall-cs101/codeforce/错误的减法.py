a,b=map(int,input().split())
for i in range(0,b):
    if a==1:
        break
    elif a%10!=0:
        a-=1
    elif a%10==0:
        a=a//10
print(a)