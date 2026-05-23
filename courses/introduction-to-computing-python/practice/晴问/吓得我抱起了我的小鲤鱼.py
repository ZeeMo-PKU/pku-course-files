def liyv(n):
    if n==0:
        return '我的小鲤鱼'
    else:
        return '抱着'+liyv(n-1)+'的我'
n=int(input())
print('吓得我抱起了'+liyv(n))