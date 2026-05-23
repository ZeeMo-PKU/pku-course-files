
while True:
    N=int(input())
    if N==0:
        break
    nums=[]
    for i in range(0,N):
        nums.append(int(input()))
    nums.sort()
    if N%2==1:
        print(nums[N//2])
    else:
        ans=nums[N//2]+nums[N//2-1]
        ans//=2
        print(ans)