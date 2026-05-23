kk=input()
a=input()
n=0
for i in range(0,len(a)-1):
    if a[i]==a[i+1]:
        n+=1
print(n)