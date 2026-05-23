a=int(input())
b=str(bin(a))
c=b[2::]
n=0
for i in range(0,len(c)):
    if c[i]==c[-i-1]:
        n+=1
if n==len(c):
    print('Yes')
else:
    print('No')