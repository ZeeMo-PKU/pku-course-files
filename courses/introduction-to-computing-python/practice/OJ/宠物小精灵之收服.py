# n,m,k=map(int,input().split())
# dp=[[[0]*(n+1) for _ in range(0,m+1)] for a in range(0,k+1)]
#
# N=[0]
# M=[0]
# for i in range(0,k):
#     n1,m1=map(int,input().split())
#     N.append(n1)
#     M.append(m1)
#
# for kk in range(1,k+1):
#     for km in range(1,m+1):
#         for kn in range(1,n+1):
#             if kn-N[kk]>=0 and km-M[kk]>=0:
#                 dp[kk][km][kn]=max(dp[kk-1][km][kn],1+dp[kk-1][km-M[kk]][kn-N[kk]])
#             else:
#                 dp[kk][km][kn] = dp[kk - 1][km][kn]
# out=dp[-1][-1][-1]
# print(out,end=' ')
# def a():
#     for uuu in range(1,m+1):
#         if dp[-1][uuu][-1]==out:
#             return m-uuu
#     return m
# if out==0:
#     print(m)
# else:
#     print(a())


n,m,k=map(int,input().split())
dp=[[0]*(n+1) for a in range(0,m+1)]




for kk in range(1,k+1):
    n1, m1 = map(int, input().split())
    for km in range(m,0,-1):
        for kn in range(n,0,-1):
            if kn-n1>=0 and km-m1>=0:
                dp[km][kn]=max(dp[km][kn],1+dp[km-m1][kn-n1])
                if dp[km][kn]==k:
                    break
            # else:
            #     dp[km][kn] = dp[km-1][kn-1]
out=dp[-1][-1]
print(out,end=' ')
def a():
    for uuu in range(0,m+1):
        if dp[uuu][-1]==out:
            return m-uuu
    return m
if out==0:
    print(m)
else:
    print(a())
# print(dp)








