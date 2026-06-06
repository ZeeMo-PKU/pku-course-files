#失败的，考虑不了平局
while True:
    n=int(input())
    n1=n
    if n==0:
        break
    tian_horses=list(map(int,input().split()))
    guowang_horses=list(map(int,input().split()))
    win=0
    pingju=0
    tian_horses.sort(reverse=True)
    guowang_horses.sort(reverse=True)
    print(guowang_horses, tian_horses)
    for i in tian_horses:
        for j in range(0,n):
            if i>guowang_horses[j]:
                win+=1
                guowang_horses[j]=float('inf')
                break
            if j==n-1 and i==guowang_horses[j]:
                pingju+=1
                a=guowang_horses.pop(-1)
                n-=1
    print(guowang_horses, tian_horses)
    print((2*win-n1+pingju)*200)
    print(win,n1,pingju)
#答案
for _ in range(50):
    n = int(input())
    if n == 0:
        break
    A = [[], []]
    for _ in range(n):  # 田忌赛马这个题目，测试数据更新过，已经不用这么复杂来接收。常用读入数据的方法就可以。
        for x in input().split():
            A[0].append(int(x))
        if len(A[0]) == n:
            break
    for _ in range(n):
        for y in input().split():
            A[1].append(int(y))
        if len(A[1]) == n:
            break

    A[0].sort(reverse=True)
    A[1].sort(reverse=True)

    answer = 0

    for _ in range(n):
        if A[0][0] > A[1][0]:
            answer += 1
            del A[0][0]
            del A[1][0]
        else:
            if A[0][-1] > A[1][-1]:
                answer += 1
                del A[0][-1]
                del A[1][-1]
            else:
                if A[0][-1] < A[1][0]:
                    answer -= 1
                del A[0][-1]
                del A[1][0]

    print(200 * answer)