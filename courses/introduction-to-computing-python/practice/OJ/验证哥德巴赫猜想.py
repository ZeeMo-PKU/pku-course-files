Q=[i for i in range(1,1000)]
zhishu=[]
op=0
for i in range(2,2000):
    for j in range(1,i+1):
        if i%j:
           op+=1
    if op==i-2:
       zhishu.append(i)
    if True:
       op=0
b=eval(input())
if b<6 or b%2!=0:
    print('Error!')
else:
    for c in zhishu:
       if b-c in zhishu:
        print(f'{b}={c}+{b-c}')
        zhishu.remove(b-c)
    else:
        pass
    
    
