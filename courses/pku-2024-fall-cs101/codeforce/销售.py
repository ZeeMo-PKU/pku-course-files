a,b=map(int,input().split())
user_input = input()
input_list = [int(x) for x in user_input.split()]
money=0
kk=0
input_list.sort()
while kk<b:
    if int(input_list[0])<0:
        money+=int(input_list.pop(0))
        kk+=1
    else:
        break
print(-money)