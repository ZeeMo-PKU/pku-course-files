s=input()
m=0
n=len(s)
out=[]

while 2**m<=n:
    out.append(s[2**m-1])
    m+=1

l=len(out)

zuo=0
you=l-1

while zuo<you:
    print(out[zuo],end='')
    print(out[you],end='')
    zuo+=1
    you-=1
if zuo==you:
    print(out[zuo])