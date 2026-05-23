#greedy
def army(money,b):
    mine=0
    his=0
    if b[0]>money:
        return 0
    while len(b)>1:
        if money>=b[0]:
            money-=b.pop(0)
            mine+=1
        else:
            his+=1
            money+=b.pop(-1)
    if b[0]<money:
        mine+=1
    return mine-his


money=int(input())
b=list(input().split())
b=[int(i) for i in b ]
b.sort()
print(army(money,b))