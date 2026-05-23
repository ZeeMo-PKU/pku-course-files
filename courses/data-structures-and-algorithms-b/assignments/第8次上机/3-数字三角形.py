# 超时
# def dfs(my_list,value,position,step,n):
#     global ans
#     if step==n:
#         ans=max(ans,value)
#         return
#     else:
#         dfs(my_list,value+my_list[step+1][position+1],position+1,step+1,n)
#         dfs(my_list,value+my_list[step+1][position],position,step+1,n)
# n=int(input())
# nums=[[0]]
# for i in range(1,n+1):
#     nums.append(list(map(int,input().split())))
# ans=0
# dfs(nums,nums[1][0],0,1,n)
# print(ans)
#
#超内存
# from collections import deque
# n=int(input())
# nums=[[0]]
# for i in range(1,n+1):
#     nums.append(list(map(int,input().split())))
# ans=0
# A=deque()
# A.append((nums[1][0],0,1))
# while A:
#     (value,position,step)=A.popleft()
#     if step==n:
#         ans=max(ans,value)
#     else:
#         A.append((value+nums[step+1][position],position,step+1))
#         A.append((value+nums[step+1][position+1],position+1,step+1))
# print(ans)


n=int(input())
dp=[[0]]
for i in range(1,n+1):
    u=list(map(int,input().split()))
    dp.append(u)
for row in range(n,1,-1):
    for col in range(0,len(dp[row])-1):
        dp[row-1][col]+=max(dp[row][col],dp[row][col+1])
print(dp[1][0])




