while True:
    b,n=map(int,input().split())
    if (n,b)==(-1,-1):
        break

    jundui=list(map(int,input().split()))

    jundui.sort()

    i=0
    out=0
    while i<n:

        zuizuoduan=jundui[i]

        while i<n and jundui[i]-zuizuoduan<=b:
            i+=1

        i-=1

        xuanzedian=jundui[i]
        while i<n and jundui[i]-xuanzedian<=b:
            i+=1
        out+=1
    print(out)



