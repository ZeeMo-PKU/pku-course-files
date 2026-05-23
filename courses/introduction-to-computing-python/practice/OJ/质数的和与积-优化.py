n=int(input())
def shibushizhishu(a):
    for j in range(2, int(a**0.5) + 1):
        if a % j == 0:
            return False
    return True
for i in range(n//2,n):
    if shibushizhishu(i) and shibushizhishu(n-i):
        print(i*(n-i))
        break