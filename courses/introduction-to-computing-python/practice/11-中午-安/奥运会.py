n=int(input())
gold=0
yin=0
tong=0

for i in range(0,n):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    gold+=a
    yin+=b
    tong+=c
print(gold,yin,tong,gold+yin+tong)