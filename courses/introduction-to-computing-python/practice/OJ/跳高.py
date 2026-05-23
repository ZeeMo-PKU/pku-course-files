
# # nums.reverse()
#
# #求最大递减子序列
# xvlie=[]
#
# # f=[1]*n
# # for i in range(1,n):
# #     for j in range(0,i):
# #         if nums[i]<nums[j]:
# #             f[i]=max(f[j]+1,f[i])
# #
# # print(max(f))
# # print(f)
n=int(input())
nums=list(map(int,input().split()))
nums.reverse()
from bisect import bisect_left
tiaogaoqi=[]
l=0
for kk in range(0,n):
    suoyin=bisect_left(tiaogaoqi,nums[kk])
    if suoyin==l:
        tiaogaoqi.append(nums[kk])
        l+=1
    else:tiaogaoqi[suoyin]=nums[kk]
print(l)


