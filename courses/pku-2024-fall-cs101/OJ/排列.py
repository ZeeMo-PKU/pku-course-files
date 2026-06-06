m=int(input())
for i in range(0,m):
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))

    for j in range(0,k):
        i=n-1
        while i-1>=0:
            if nums[i-1]>nums[i]:
                i-=1
                continue
            else:

                k=n-1
                while True:
                    if nums[k]>nums[i-1]:
                        nums[k],nums[i-1]=nums[i-1],nums[k]
                        break
                    else:
                        k-=1
                left=i
                right=n-1
                while left<right:
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
                    right-=1
                break
        if i==0:
            nums=[_ for _ in range(1,n+1)]
    print(*nums)
