def make_24(my_list):
    if len(my_list)==1 :
        if abs(my_list[0]-24)<1e-5:
            return True
        else:
            return False
    else:
        for i in range(0,len(my_list)):
            for j in range(0,len(my_list)):
                if i!=j:
                    a=my_list[i]
                    b=my_list[j]
                    left=[]
                    for z in range(0,len(my_list)):
                        if z!=i and z!=j:
                            left.append(my_list[z])
                    if make_24(left+[a+b]) or make_24([a-b]+left) or make_24([a*b]+left):
                        return True
                    if b!=0 and make_24([a/b]+left):
                        return True
        return False
while True:
    a,b,c,d=map(int,input().split())
    if a==0:
        break
    else:
        my_list=[a,b,c,d]
        if make_24(my_list):
            print('YES')
        else:
            print('NO')