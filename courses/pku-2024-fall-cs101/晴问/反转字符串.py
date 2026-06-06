def fanchuan(a):
    if len(a)==1:
        return a
    return fanchuan(a[1:])+a[0]
a=input()
print(fanchuan(a))