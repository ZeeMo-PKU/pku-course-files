while True:
    try:
        a, b = map(int, input().split())
        gcd = min(a, b)
        for i in range(gcd, 0, -1):
            if a % i == 0 and b % i == 0:
                print(i)
                break

    except EOFError:
        break