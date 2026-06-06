kkk=input()
a=0
d=0
w=input()
for i in range(0,len(w)):
    if w[i]=='A':
        a+=1
    else:
        d+=1
if a>d:
    print('Anton')
elif a<d:
    print('Danik')
else:
    print('Friendship')
