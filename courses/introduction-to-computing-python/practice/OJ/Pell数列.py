def pell(a):
    aou=0
    aji=1
    for i in range(0,a//2+a%2):
        aji=(2*aou+aji)%32767
        aou=(2*aji+aou)%32767
    if a%2:
        return aji
    else:
        return aou
n=int(input())
for j in range(0,n):
    print(pell(int(input())))