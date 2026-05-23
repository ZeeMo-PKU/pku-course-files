def abc(n,first,second,third):
    u=0
    if n==0:
        return
    abc(n-1,first,third,second)
    print(f'{first}->{third}')
    u+=1
    abc(n-1,second,first,third)
n=int(input())
print(2**n-1)
abc(n,'A','B','C')