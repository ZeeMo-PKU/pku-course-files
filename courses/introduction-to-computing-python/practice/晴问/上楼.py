def shanglou(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return shanglou(n-1)+shanglou(n-2)
n=int(input())
print(shanglou(n))