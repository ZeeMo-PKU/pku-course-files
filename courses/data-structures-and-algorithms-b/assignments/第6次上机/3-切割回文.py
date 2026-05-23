def huiwen(b):
    if b[::-1]==b:
        return True
    else:
        return False
def main(a):
    l=len(a)
    if l==1:
        return 1
    if l==0:
        return 0
    for i in range(l,0,-1):
        if huiwen(a[0:i]):
            return 1+main(a[i:])

T=int(input())
for i in range(T):
    a=input()
    print(main(a)-1)