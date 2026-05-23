N,D=map(int,input().split())
h=[]
for i in range(0,N):
    h.append(int(input()))
used=[0]*N
while 0 in used:
    free=[]
    for j in range(N):
        if h[i]:
            continue
        if not free:
            minv=h[i]
            maxv=h[i]
        else:
            if h[i]>maxv:
                maxv=h[i]
            if h[i]<minv:
                minv=h[i]
        if maxv-minv>2*D:
            break
        if h[i]+D>=maxv and h[i]-D<=minv:
            free.append(h[i])
            used[i]=1
    free.sort()
    print('\n'.join(map(str,free)))
