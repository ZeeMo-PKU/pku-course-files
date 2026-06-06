a=input()
n=0
m=0
for i in range(0,len(a)):
    if a[i]=='4' or a[i]=='7':
        n+=1
n=str(n)
for j in range(0,len(n)):
    if n[j]!='4' and n[j]!='7':
        print('NO')
        break
    else:
        m+=1
if m==len(n):
    print('YES')