num=int(input())
children=input()
a=[int(i) for i in children.split()]
num_1=a.count(1)
num_2=a.count(2)
num_3=a.count(3)
num_4=a.count(4)
sum_=0
sum_+=num_4#统计4
if num_3>=num_1:#统计3和1
    sum_+=num_3
    num_1=0
else:
    num_1=num_1-num_3
    sum_+=num_3
sum_+=((num_1+2*num_2)//4)
if (num_1+2*num_2)%4!=0:
    sum_+=1
print(sum_)