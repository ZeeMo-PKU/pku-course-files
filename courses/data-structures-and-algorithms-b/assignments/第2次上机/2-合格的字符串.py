n=int(input())
zuoyes=['1']
zuoye2=[1]
for i in range(1,n+1):
    a=input()
    zuoye2.append(a)
    zuoye=[i.lower() for i in list(a)]
    zuoyes.append(zuoye)

b=input()
moban=[i.lower() for i in b]

zuo=-1
you=-1
for i in range(0,len(moban)):
    if moban[i]=='[':
        moban_zuo=moban[0:i]
        zuo=i
    elif moban[i]==']':
        moban_you=moban[i+1:len(moban)]
        you=i
neirong=moban[zuo+1:you]
l_neirong=len(neirong)
changdu=len(moban_zuo)+len(moban_you)+1
for i in range(1,n+1):
    zuoye=zuoyes[i]
    if len(zuoye)!=changdu:
        continue
    elif zuoye[0:zuo]!=moban_zuo or zuoye[you-l_neirong:]!=moban_you:
        continue
    elif zuoye[zuo] in neirong:
        print(f'{i} {zuoye2[i]}')