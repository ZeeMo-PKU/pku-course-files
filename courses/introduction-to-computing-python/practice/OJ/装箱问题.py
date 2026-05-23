import math
while True:
    out=0
    num1,num2,num3,num4,num5,num6=map(int,input().split())
    if {num1,num2,num3,num4,num5,num6}=={0}:
        break
    #处理3，4，5，6
    out+=num6
    out+=num5
    out+=num4
    out+=math.ceil(num3/4)
    #刷新3

    #装2的空位

    num3_ = num3 % 4
    num2_=0
    num2_+=num4*5
    if num3_==1:
        num2_+=5
    elif num3_==2:
        num2_+=3
    elif num3_==3:
        num2_+=1
    if num2>num2_:
        out+=math.ceil((num2-num2_)/9)

    num1-=out*36-num6*36-num5*25-num4*16-num3*9-num2*4
    if num1>0:
        out+=math.ceil(num1/36)
    print(out)

