a=int(input())
_=0
for i in range(0,a):
    b=input()
    _+=int(b.count('###')/2)-b.count('### ###')
print(_)