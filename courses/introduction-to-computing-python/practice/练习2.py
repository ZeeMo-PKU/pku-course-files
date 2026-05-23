def f(a):
    if a=='1':
        return True
    else:
        return False
aaa=False
for i in range(0,3):
    b=f(input())
    print(b)
    aaa=b or aaa
    print(aaa)