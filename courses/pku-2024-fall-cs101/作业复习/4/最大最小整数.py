#冒泡排序
#错误思路
import copy
n=int(input())
nums=list(map(str,input().split()))
for i in range(0,n):
    for j in range(0,n-i-1):
        uuu=min(len(nums[j]), len(nums[j + 1]))
        for op in range(0,uuu):
            if nums[j+1][op]>nums[j][op]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                break
            elif nums[j+1][op]<nums[j][op]:
                break
            if op==uuu-1 and len(nums[j])>=len(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(''.join(nums),end=' ')
print(''.join(reversed(nums)))
########
n = int(input())
nums = input().split()
for i in range(n - 1):
    for j in range(i+1, n):
        #print(i,j)
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))