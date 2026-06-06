def jiecheng(n):
    if n==0:
        return 1
    else:
        return n*jiecheng(n-1)
n=int(input())
print(jiecheng(n))