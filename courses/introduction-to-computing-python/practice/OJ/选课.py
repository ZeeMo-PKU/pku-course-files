def nextPermutation(nums,a):
    i = a - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = a - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, a - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
a=int(input())
b=int(input())
nums=list(map(int,input().split()))
for uuu in range(0,b):
    nextPermutation(nums,a)
print(*nums)