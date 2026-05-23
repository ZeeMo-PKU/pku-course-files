from collections import Counter

dic={'A':'2','B':'2','C':'2',
     "D":'3','E':'3','F':'3',
     'G':'4','H':'4','I':'4',
     'J':'5','K':'5','L':'5',
     'M':'6','N':'6','O':'6',
     'P':'7','R':'7','S':'7',
     'T':'8','U':'8','V':'8',
     'W':'9','X':'9','Y':'9'
     }

group=[]

n=int(input())
for i in range(0,n):
    nums=input()
    telephone_number = ''

    for number in nums:
        #跳过
        if number=='-':
            continue
        #数字
        elif '0'<=number<='9':
            telephone_number+=number
        else:
            telephone_number+=dic[number]

    group.append(telephone_number[0:3]+'-'+telephone_number[3:])
#print(group)
dic=dict(Counter(group))
dic=sorted(dic.items(),key=lambda item:item[0])
dic=dict(dic)

u=0

for key, value in dic.items():
    if value>1:
        print(key+' '+str(value))
        u=1

if not u:
    print('No duplicates.')



