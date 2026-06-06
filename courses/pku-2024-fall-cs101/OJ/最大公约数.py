from math import gcd
while True:
    try:
        m,n=map(int,input().split())
        print(gcd(m,n))
    except EOFError:
        break