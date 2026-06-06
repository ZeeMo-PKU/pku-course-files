import math
#math.sqrt()
#math.asin()
def f(A,B,C,D):
    a1=A*math.asin(math.sqrt(B)/2)
    a2=C*math.asin(math.sqrt(D)/2)
    if abs(a1-a2)<1e-5:
        return 0
    else:
        if a1-a2>0:
            return 1
        else:
            return 2
A,B,C,D=map(int,input().split())
print(f(A,B,C,D))