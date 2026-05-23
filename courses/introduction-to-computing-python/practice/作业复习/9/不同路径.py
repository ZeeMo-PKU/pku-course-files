# #dfs
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         fangxiang={(1,0),(0,-1)}
#         import sys
#         sys.setrecursionlimit(990000)
#         num=0
#         def dfs(x,y):
#             global num
#             if x==n-1 and y==m-1:
#                 num+=1
#                 return
#             for (dx,dy) in fangxiang:
#                 if x+dx<n and y+dy<m:
#                     dfs(x+dx,y+dy)
#         dfs(0,0)
#         print(num)
#dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n]
        for i in range(1,m):
            dp.append([1]+[0]*(n-1))
        dp[0][0]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]