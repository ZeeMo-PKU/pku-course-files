#先将中缀表达式转换为后缀表达式-利用调度场算法
#一些类别：
fuhaos={'+','-','*','/'}
shuzi={'.','1','2','3','4','5','6','7','8','9','0'}
#比较优先级的函数
def youxianji(x):
    if x in {'*','/'}:
        return 3
    elif x in {'+','-'}:
        return 2
    return 1
#正常的计算函数
def jisuan(a,fuhao,b):
    if fuhao=='+':
        return a+b
    elif fuhao=='-':
        return a-b
    elif fuhao=='*':
        return a*b
    else:
        if b!=0:
            return a/b
#主函数
def main(juzi):
    ans=0
    l=len(juzi)
    i=0
    zhan_shuzi=[]
    zhan_fuhao=[]

    while i<l:
        if juzi[i] in shuzi:
            now_number_str=''
            while i<l and juzi[i] in shuzi:
                now_number_str=now_number_str+juzi[i]
                i+=1
                continue
            # 记录数字
            now_number = float(now_number_str)
            zhan_shuzi.append(now_number)
        else:
            if i<l:
                #记录括号
                if juzi[i]=='(':
                    zhan_fuhao.append('(')
                elif juzi[i]==')':
                    while zhan_fuhao and zhan_fuhao[-1]!='(':
                        b = zhan_shuzi.pop()
                        a = zhan_shuzi.pop()
                        op = zhan_fuhao.pop()
                        zhan_shuzi.append(jisuan(a, op, b))
                    zhan_fuhao.pop()
                #记录符号
                elif juzi[i] in fuhaos:
                    while zhan_fuhao and  youxianji(zhan_fuhao[-1])>=youxianji(juzi[i]):
                        b = zhan_shuzi.pop()
                        a = zhan_shuzi.pop()
                        op = zhan_fuhao.pop()
                        zhan_shuzi.append(jisuan(a, op, b))
                    zhan_fuhao.append(juzi[i])

                i += 1
                continue
    #最后
    if i==l:
        while zhan_fuhao:
            b=zhan_shuzi.pop()
            a=zhan_shuzi.pop()
            op=zhan_fuhao.pop()
            zhan_shuzi.append(jisuan(a,op,b))
    #输出
    return f'{zhan_shuzi[0]:.2f}'
juzi=input()
print(main(juzi))