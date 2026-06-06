def f(list1, k):
    if list1[-1][0]-list1[0][0]<=k:
        return max(list1, key=lambda x: x[1])[1]
    for j in range(0,99):
        if list1[j][0]-list1[0][0]>11:
            break
        aaa=[]
        for u in range(j+1,99):
            if list1[u][0]-list1[j][0]>11:
                aaa.append(list1[j][1] + f(list1[u:], k))
                break
        return max(aaa)
T=int(input())
for i in range(0,T):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    list1=[]
    for j in range(0,n):
        list1.append((m[j],p[j]))
    #print(list1)
    print(f(list1,k))
