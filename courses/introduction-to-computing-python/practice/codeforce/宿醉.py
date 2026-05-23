while True:
    a=eval(input())
    if a==0.00:
        break
    else:
        for i in range(2,99999999099999):
            a=a-1/i
            if a<=0:
                print(f'{i-1} card(s)')
                break