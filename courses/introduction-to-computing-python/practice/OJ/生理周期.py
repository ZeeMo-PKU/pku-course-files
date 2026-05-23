op=0
while True:
    op+=1
    a,b,c,d=map(int,input().split())
    if a==-1 and b==-1 and c==-1 and d==-1:
        break
    else:
        for i in range(1,9999999):
            if (d+i-a)%23==0 and (d+i-b)%28==0 and (d+i-c)%33==0:
                print(f'Case {op}: the next triple peak occurs in {i} days.')
                break