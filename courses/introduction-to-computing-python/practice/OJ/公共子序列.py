# # def f(A,B,num):
# #
# #     for i in range(0,len(A)):
# #         if A[i] in B:
# #             uu=B.index(A[i])
# #             if uu==len(B)-1:
# #                 return num+1
# #             return f(A[i+1:],B[uu+1:],num+1)
# #         if i==len(A)-1 and A[-1] not in B:
# #             return num
# #         elif i==len(A)-1 and A[-1] in B:
# #             return
# #     return num
# # while True:
# #     try:
# #         A,B=input().split()
# #
# #         out=[0]
# #         for i in range(0,len(A)):
# #             out.append(f(A[i:],B,0))
# #         print(out)
# #
# #     except EOFError:
# #         break
# while True:
#     try:
#         # 读取输入并去除首尾空白字符
#         input_line = input().strip()
#         if not input_line:
#             continue
#
#         # 分割输入字符串
#         str1, str2 = input_line.split()
#
#         # 获取字符串长度
#         len1, len2 = len(str1), len(str2)
#
#         # 初始化动态规划表
#         dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]
#
#         # 填充动态规划表
#         for i in range(1, len1 + 1):
#             for j in range(1, len2 + 1):
#                 if str1[i - 1] == str2[j - 1]:
#                     dp_table[i][j] = dp_table[i - 1][j - 1] + 1
#                 else:
#                     dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
#                 print(dp_table)
#
#         # 输出最长公共子序列的长度
#         print(dp_table[len1][len2])
#
#     except EOFError:
#         break
while True:
    try:
        A,B=input().split()
        L_A=len(A)
        L_B=len(B)
        dp=[]
        for i in range(0,L_A+1):
            dp.append([0]*(L_B+1))
        for i in range(1,L_A+1):
            for j in range(1,L_B+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        print(dp[-1][-1])


    except EOFError:
        break
