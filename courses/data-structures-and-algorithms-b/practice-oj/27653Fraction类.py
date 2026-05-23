#最大公因数是什么
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b,c,d=map(int,input().split())
x=a*d+b*c
y=b*d
u=gcd(x,y)
x=int(x/u)
y=int(y/u)
print(f'{x}/{y}')