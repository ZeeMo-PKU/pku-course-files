def huiwen(a):
    if len(a)<3:
        if a[0]!=a[-1]:
            return 'No'
        else:
            return 'Yes'
    if a[0]==a[-1]:
        return huiwen(a[1:-1])
    return 'No'
a=input()
print(huiwen(a))