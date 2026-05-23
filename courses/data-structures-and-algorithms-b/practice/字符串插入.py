while True:
    try:
        a, b = input().split()
        A = list(a)
        A.sort()
        a1 = A[-1]
        for i in range(len(a)):
            if a[i] == a1:
                break
        print(a[0:i + 1] + b + a[i + 1:])
    except EOFError:
        break


