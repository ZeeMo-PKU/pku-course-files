a=input()
n=0
for i in range(0,len(a)):
    k=a[i]
    l=k.lower()
    if k==l:
        n+=1
if n>=len(a)-n:
    for j in range(0,len(a)):
        op=a[j].lower()
        print(f'{op}',end='')
else:
    for ou in range(0,len(a)):
        po=a[ou].upper()
        print(f'{po}',end='')
