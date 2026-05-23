def is_prime(n):
    """判断一个数是否为质数"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
import math
num=int(input())
b=input()
for i in b.split():
    if int(math.sqrt(int(i)))**2!=int(i):
        print('NO')
    else:
        if is_prime(int(math.sqrt(int(i)))):
            print('YES')
        else:
            print('NO')
