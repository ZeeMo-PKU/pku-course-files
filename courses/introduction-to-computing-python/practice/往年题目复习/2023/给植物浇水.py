n,a,b=map(int,input().split())
shui=list(map(int,input().split()))
zuo=0
you=n-1
A=a
B=b
out=0
while zuo<you:
    if shui[zuo]>A:
        out+=1
        A=a-shui[zuo]
    elif shui[zuo]<A:
        A-=shui[zuo]
    zuo+=1
    if shui[you]>B:
        out+=1
        B=b-shui[you]
    elif shui[you]<B:
        B-=shui[you]
    you-=1
if zuo==you and max(A,B)<shui[zuo]:
    out+=1
print(out)
