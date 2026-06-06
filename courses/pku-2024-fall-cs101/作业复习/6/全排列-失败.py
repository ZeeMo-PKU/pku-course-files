# #下一个排列-模版
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         i = len(nums) - 2
#         while i >= 0 and nums[i] >= nums[i + 1]:
#             i -= 1
#         if i >= 0:
#             j = len(nums) - 1
#             while j >= 0 and nums[i] >= nums[j]:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]
#
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1
#
#
# 作者：力扣官方题解
# 链接：https: // leetcode.cn / problems / next - permutation / solutions / 479151 / xia - yi - ge - pai - lie - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
# def nextPermutation(nums):
#     i = len(nums) - 2
#     while i >= 0 and nums[i] >= nums[i + 1]:
#         i -= 1
#     if i >= 0:
#         j = len(nums) - 1
#         while j >= 0 and nums[i] >= nums[j]:
#             j -= 1
#         nums[i], nums[j] = nums[j], nums[i]
#
#     left, right = i + 1, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
jieguo=[]
n=int(input())
def quanpailie(nums,kaishi):

    if kaishi==n-1:
        jieguo.append(list(nums))

    for i in range(kaishi,n):
        nums[kaishi],nums[i]=nums[i],nums[kaishi]
        quanpailie(nums,kaishi+1)
        nums[kaishi], nums[i] = nums[i], nums[kaishi]

nums=[_ for _ in range(1,n+1)]
quanpailie(nums,0)
paixv=[[i] for i in range(0,n)]
jieguo.sort()
for i in jieguo:
    print(*i)
a.sort()
b=[]
for j in range(0,len(a)-1):
    b.append(a[j+1]-a[j])