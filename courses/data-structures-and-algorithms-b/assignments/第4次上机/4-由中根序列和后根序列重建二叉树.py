def f(zhong:list,hou:list):
    if zhong==[] or hou==[]:
        return zhong+hou
    gen=hou[-1]
    gen_suoyin=zhong.index(gen)
    return [gen]+f(zhong[:gen_suoyin],hou[:gen_suoyin])+f(zhong[gen_suoyin+1:],hou[gen_suoyin:-1])

zhong=list(map(int,input().split()))
hou=list(map(int,input().split()))
print(*f(zhong,hou))