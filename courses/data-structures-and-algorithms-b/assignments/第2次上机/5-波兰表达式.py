def jisuan(num1,num2,fuhao):
    if fuhao=='+':
        return num1+num2
    if fuhao=='-':
        return num1-num2
    if fuhao=='*':
        return num1*num2
    if fuhao=='/':
        return num1/num2
juzi=list(input().split(' '))
fuhao=set('+-*/')
l=len(juzi)

shu=[]

for i in range(-1,-l-1,-1):
    if juzi[i] in fuhao:
        num1=shu.pop()
        num2=shu.pop()
        num3=jisuan(num1,num2,juzi[i])
        shu.append(num3)

    else:
        shu.append(float(juzi[i]))

print(f'{shu[-1]:.6f}')