#递归
op=0
def hannuota(a,b,c,n):
    global op
    op+=1
    if n==1:
        return f'{a}->{c}'
    return (f'{hannuota(a,c,b,n-1)}'
            f'\n{a}->{c}'
            f'\n{hannuota(b,a,c,n-1)}')
n=int(input())
u=hannuota('A','B','C',n)
print(op)
print(u)