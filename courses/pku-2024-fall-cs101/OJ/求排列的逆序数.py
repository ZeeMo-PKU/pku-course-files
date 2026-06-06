#时间复杂度太高了
n=int(input())
out=0
nums=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            out+=1
print(out)
#运用二分法
