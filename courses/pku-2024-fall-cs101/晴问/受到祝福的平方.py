import math
def shibushi(a):
    if int(a)==0:
        return False

    if math.isqrt(int(a))**2==int(a):
        return True
    return False

A=str(input())
s=len(A)

uuu=False
def dfs(str1,lens):
    global uuu
    if uuu:
        return
    if shibushi(str1):
        uuu = True
    for i in range(1,lens):
        if shibushi(str1[:i]):
            dfs(str1[i:],lens-i)

dfs(A,s)
if uuu:
    print('Yes')
else:
    print('No')

