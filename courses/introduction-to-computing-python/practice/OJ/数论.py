def euler_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []  # 用于存储素数
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes
u=euler_sieve(1000000)
def ijn(k):
    list1=0
    for op in u:
        if k==(k//op)*op:
            list1+=1
            k=k//op
            if k==(k//op)*op:
                return 0
    if list1%2==0:
        return 1
    if list1%2==1:
        return -1
print(ijn(int(input())))
  


