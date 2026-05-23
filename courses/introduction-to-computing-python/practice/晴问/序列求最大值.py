
def abc(n,a):
    if n==1:
        return sum(a)
    if a[0]>a[-1]:
        return abc(n-1,a[:-1])
    else:
        return abc(n-1,a[1:])

n = int(input())
a=input().split()
a=[int(i) for i in a]
print(abc(n,a))