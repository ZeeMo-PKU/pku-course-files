import math

def taoli(names,huilv):
    for qidian in huilv:
        for zhongdian in huilv[qidian]:
            a=huilv[qidian][zhongdian]
            huilv[qidian][zhongdian]=-math.log(a)
    l=len(names)
    xvhao={}
    for i in range(0,l):
        xvhao[names[i]] = i

    dp = [[float('inf')] * l for _ in range(l)]

    for A in huilv:
        for B in huilv[A]:
            dp[xvhao[A]][xvhao[B]]=huilv[A][B]
    for i in range(0,l):
        dp[i][i]=0
    for k in range(l):
        for i in range(l):
            for j in range(l):

                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for i in range(0,l):
        if dp[i][i] < -1e-9:
            return True
    return False

case=1
while True:
    n=int(input())
    if n==0:
        break
    names=[]
    for i in range(n):
        names.append(input())

    huilv={name:{} for name in names}
    m=int(input())
    for i in range(m):
        A,num,B=input().split()
        num=float(num)
        huilv[A][B]=num

    if taoli(names,huilv):
        print(f'Case {case}: Yes')
    else:
        print(f'Case {case}: No')
    case+=1
    a=input()








#
#
#
#
#
#
#
#
# import math
#
# def has_arbitrage(names, exchange_rates):
#     num_nodes = len(names)
#     index_map = {name: idx for idx, name in enumerate(names)}
#
#     # 初始化距离矩阵为无穷大
#     dp = [[float('inf')] * num_nodes for _ in range(num_nodes)]
#     for i in range(num_nodes):
#         dp[i][i] = 0  # 自环权重为0
#
#     # 构建图：将汇率转换为 -log(rate)
#     for src in exchange_rates:
#         for dst in exchange_rates[src]:
#             rate = exchange_rates[src][dst]
#             dp[index_map[src]][index_map[dst]] = -math.log(rate)
#
#     # Floyd-Warshall 算法
#     for k in range(num_nodes):
#         for i in range(num_nodes):
#             for j in range(num_nodes):
#                 if dp[i][k] + dp[k][j] < dp[i][j]:
#                     dp[i][j] = dp[i][k] + dp[k][j]
#
#     # 检查是否有负权环
#     for i in range(num_nodes):
#         if dp[i][i] < -1e-9:  # 加上小容差避免精度问题
#             return True
#     return False
#
# # 主程序
# import sys
#
# def main():
#     case_num = 1
#     lines = [line.strip() for line in sys.stdin if line.strip()]
#     ptr = 0
#
#     while ptr < len(lines):
#         n = int(lines[ptr])
#         ptr += 1
#         if n == 0:
#             break
#
#         names = []
#         for _ in range(n):
#             names.append(lines[ptr])
#             ptr += 1
#
#         m = int(lines[ptr])
#         ptr += 1
#
#         exchange_rates = {name: {} for name in names}
#         for _ in range(m):
#             parts = lines[ptr].split()
#             A, rate, B = parts[0], float(parts[1]), parts[2]
#             ptr += 1
#             exchange_rates[A][B] = rate
#
#         if has_arbitrage(names, exchange_rates):
#             print(f'Case {case_num}: Yes')
#         else:
#             print(f'Case {case_num}: No')
#         case_num += 1
#
# if __name__ == "__main__":
#     main()