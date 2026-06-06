while True:
    n=int(input())
    if n==0:
        break

    jiudian=[]
    for i in range(0,n):
        jiudian.append(tuple(map(int,input().split())))

    jiudian.sort(key=lambda x:(x[0],x[1]))
    out=0
    zuida=float('inf')
    for juli,jiage in jiudian:
        if jiage<zuida:
            zuida=jiage
            out+=1
    print(out)
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     # 读取并排序酒店
#     hotels = [tuple(map(int, input().split())) for _ in range(n)]
#     hotels.sort(key=lambda x: (x[0], x[1]))  # 按距离升序排序，距离相同按价格升序排序
#
#     # 初始化单调递减的价格栈
#     stack = []
#
#     # 遍历排序后的酒店
#     for d, c in hotels:
#         # 如果当前酒店的价格小于或等于栈顶的价格，弹出栈顶元素
#         while stack and c <= stack[-1]:
#             stack.pop()
#         # 将当前酒店的价格加入栈中
#         stack.append(c)
#
#     # 输出候选酒店的数量
#     print(len(stack))