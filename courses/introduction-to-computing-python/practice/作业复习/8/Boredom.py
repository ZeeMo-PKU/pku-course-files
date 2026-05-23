#dp
from collections import Counter
n=int(input())
nums=list(map(int,input().split()))
max_num=max(nums)
dic=Counter(nums)
nums_set=set(nums)
list1=[0]+[0]*max_num
for i in nums_set:
    list1[i]=i*(dic[i])
f=[0]+[0]*max_num
f[1]=list1[1]
for i in range(2,max_num+1):
    f[i]=max(f[i-1],list1[i]+f[i-2])
print(f[-1])