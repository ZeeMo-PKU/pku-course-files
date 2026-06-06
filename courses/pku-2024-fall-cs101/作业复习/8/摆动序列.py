n=int(input())
nums=list(map(int,input().split()))
if n==1:
    print(1)
else:
    ans=0
    chazhi=[]
    for i in range(1,n):
        if nums[i]-nums[i-1]!=0:
            chazhi.append(nums[i]-nums[i-1])
    if len(chazhi) in (0,1):
        ans=len(chazhi)

    else:
        ans=1
        jiyi=chazhi[0]
        for i in range(1,len(chazhi)):
            if chazhi[i]*jiyi<0:
                ans+=1
                jiyi=chazhi[i]
    # print(chazhi)
    print(ans+1)