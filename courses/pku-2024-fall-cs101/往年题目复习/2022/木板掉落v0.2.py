H,L,n=map(int,input().split())
xiaoqiu=list(map(int,input().split()))
_=len(xiaoqiu)
xiaoqiu.sort()
uuu=_//2


kkk=xiaoqiu[uuu]
# print(kkk,5*L*L/(kkk**2))
h=H-(5*L*L/(kkk**2))
print(f"{h:.2f}")