dic={}
while True:
    a=input()
    if a=='e':
        break
    elif a[0]=='a':
        a1,a2,a3=a.split()
        dic[a2]=a3
    else:
        a1,a2=a.split()
        try:
            print(dic[a2])
        except:
            print('Not')