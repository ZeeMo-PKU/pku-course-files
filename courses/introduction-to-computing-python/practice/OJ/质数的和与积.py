def is_prime(a):
    for j in range(2, int(a**0.5) + 1):
        if a % j == 0:
            return False
    return True
n=int(input())
A=[]
for i in range(n//2+1):
    if is_prime(i) and is_prime(n-i):
        A.append(i*(n-i))
print(max(A))